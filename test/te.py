import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import matplotlib.pyplot as plt
from skimage import morphology
from skimage.filters import threshold_otsu, threshold_local
import re
import os
from concurrent.futures import ThreadPoolExecutor
import time
from typing import Tuple, List, Optional, Dict, Union


class OCRProcessor:
    def __init__(self, config_path: str = None):
        """
        初始化OCR处理器

        参数:
            config_path: 配置文件路径
        """
        self.config = {
            'preprocess': {
                'denoise': True,
                'binarization': 'adaptive',
                'adaptive_block_size': 31,
                'adaptive_c': 10,
                'scale_factor': 2.0,
                'contrast_factor': 1.5,
                'sharpness_factor': 2.0,
                'remove_small_objects': True,
                'min_object_size': 50,
                'dilate_iterations': 1,
                'erode_iterations': 1
            },
            'ocr': {
                'engine': 'tesseract',
                'lang': 'chi_sim+eng',
                'oem': 3,
                'psm': 6,
                'whitelist': None,
                'blacklist': None,
                'tessdata_dir': None,
                'char_whitelist': '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?()%$-:;/\'"'
            },
            'postprocess': {
                'spell_check': False,
                'remove_noise': True,
                'min_word_length': 2,
                'confidence_threshold': 60
            }
        }

        if config_path and os.path.exists(config_path):
            self._load_config(config_path)

        self._validate_config()

    def _load_config(self, config_path: str):
        """加载配置文件"""
        try:
            import json
            with open(config_path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)

            # 深度合并配置
            for section in self.config:
                if section in user_config:
                    self.config[section].update(user_config[section])
        except Exception as e:
            print(f"加载配置文件失败，使用默认配置: {str(e)}")

    def _validate_config(self):
        """验证配置有效性"""
        # 验证预处理配置
        preprocess = self.config['preprocess']
        if preprocess['binarization'] not in ['global', 'adaptive', 'none']:
            preprocess['binarization'] = 'adaptive'

        # 验证OCR配置
        ocr = self.config['ocr']
        if ocr['engine'] not in ['tesseract', 'easyocr', 'paddleocr']:
            ocr['engine'] = 'tesseract'

        if ocr['oem'] not in [0, 1, 2, 3]:
            ocr['oem'] = 3

        if ocr['psm'] not in range(0, 14):
            ocr['psm'] = 6

    def preprocess_image(self, image: Union[str, Image.Image, np.ndarray]) -> Image.Image:
        """
        图像预处理

        参数:
            image: 输入图像(路径、PIL图像或numpy数组)

        返回:
            预处理后的PIL图像
        """
        # 转换为PIL图像
        if isinstance(image, str):
            img = Image.open(image)
        elif isinstance(image, np.ndarray):
            img = Image.fromarray(image)
        else:
            img = image.copy()

        # 转换为RGB模式(如果是RGBA)
        if img.mode == 'RGBA':
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background

        # 获取预处理配置
        config = self.config['preprocess']

        # 1. 缩放图像
        if config['scale_factor'] != 1.0:
            new_size = (int(img.size[0] * config['scale_factor']),
                        int(img.size[1] * config['scale_factor']))
            img = img.resize(new_size, Image.LANCZOS)

        # 2. 增强对比度
        if config['contrast_factor'] != 1.0:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(config['contrast_factor'])

        # 3. 锐化图像
        if config['sharpness_factor'] != 1.0:
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(config['sharpness_factor'])

        # 转换为OpenCV格式进行高级处理
        cv_img = np.array(img)
        if len(cv_img.shape) == 3 and cv_img.shape[2] == 3:
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)

        # 4. 去噪
        if config['denoise']:
            cv_img = cv2.fastNlMeansDenoisingColored(cv_img, None, 10, 10, 7, 21)

        # 5. 二值化
        if config['binarization'] != 'none':
            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

            if config['binarization'] == 'global':
                thresh = threshold_otsu(gray)
                _, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
            else:  # adaptive
                binary = cv2.adaptiveThreshold(
                    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY_INV, config['adaptive_block_size'],
                    config['adaptive_c'])

            # 形态学操作
            kernel = np.ones((3, 3), np.uint8)
            if config['dilate_iterations'] > 0:
                binary = cv2.dilate(binary, kernel, iterations=config['dilate_iterations'])
            if config['erode_iterations'] > 0:
                binary = cv2.erode(binary, kernel, iterations=config['erode_iterations'])

            # 移除小对象
            if config['remove_small_objects']:
                binary = morphology.remove_small_objects(
                    binary > 0, min_size=config['min_object_size'], connectivity=2)
                binary = binary.astype(np.uint8) * 255

            cv_img = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

        # 转换回PIL图像
        img = Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))

        return img

    def _run_tesseract(self, image: Image.Image) -> Tuple[str, Dict]:
        """
        使用Tesseract OCR引擎识别文本

        参数:
            image: PIL图像

        返回:
            (识别文本, 元数据)
        """
        ocr_config = self.config['ocr']

        # 构建Tesseract配置字符串
        config = f'--oem {ocr_config["oem"]} --psm {ocr_config["psm"]}'

        if ocr_config['tessdata_dir']:
            config += f' --tessdata-dir "{ocr_config["tessdata_dir"]}"'

        if ocr_config['whitelist']:
            config += f' -c tessedit_char_whitelist="{ocr_config["whitelist"]}"'
        elif ocr_config['char_whitelist']:
            config += f' -c tessedit_char_whitelist="{ocr_config["char_whitelist"]}"'

        if ocr_config['blacklist']:
            config += f' -c tessedit_char_blacklist="{ocr_config["blacklist"]}"'

        # 识别文本
        text = pytesseract.image_to_string(
            image,
            lang=ocr_config['lang'],
            config=config
        )

        # 获取详细数据
        data = pytesseract.image_to_data(
            image,
            lang=ocr_config['lang'],
            config=config,
            output_type=pytesseract.Output.DICT
        )

        return text, data

    def _postprocess_text(self, text: str, confidence_data: Dict = None) -> str:
        """
        后处理识别文本

        参数:
            text: 原始识别文本
            confidence_data: 置信度数据

        返回:
            处理后的文本
        """
        post_config = self.config['postprocess']
        lines = text.split('\n')
        processed_lines = []

        for line in lines:
            # 移除空白行
            if not line.strip():
                continue

            # 移除低置信度单词
            if confidence_data and post_config['confidence_threshold'] > 0:
                words = line.split()
                confidences = confidence_data.get('conf', [])

                if len(words) == len(confidences):
                    filtered_words = [
                        word for word, conf in zip(words, confidences)
                        if int(conf) >= post_config['confidence_threshold']
                    ]
                    line = ' '.join(filtered_words)

            # 移除短单词
            if post_config['min_word_length'] > 1:
                words = line.split()
                filtered_words = [
                    word for word in words
                    if len(word) >= post_config['min_word_length']
                ]
                line = ' '.join(filtered_words)

            # 移除噪声字符
            if post_config['remove_noise']:
                line = re.sub(r'[^\w\s.,!?()%$-:;/\'"]', '', line)

            if line.strip():
                processed_lines.append(line)

        return '\n'.join(processed_lines)

    def recognize_text(self, image: Union[str, Image.Image, np.ndarray]) -> str:
        """
        识别图像中的文本

        参数:
            image: 输入图像(路径、PIL图像或numpy数组)

        返回:
            识别到的文本
        """
        # 预处理图像
        processed_img = self.preprocess_image(image)

        # 选择OCR引擎
        ocr_engine = self.config['ocr']['engine']

        if ocr_engine == 'tesseract':
            text, data = self._run_tesseract(processed_img)
        elif ocr_engine == 'easyocr':
            text = self._run_easyocr(processed_img)
            data = None
        elif ocr_engine == 'paddleocr':
            text = self._run_paddleocr(processed_img)
            data = None
        else:
            raise ValueError(f"不支持的OCR引擎: {ocr_engine}")

        # 后处理文本
        processed_text = self._postprocess_text(text, data)

        return processed_text

    def recognize_with_confidence(self, image: Union[str, Image.Image, np.ndarray]) -> Tuple[str, List[Dict]]:
        """
        识别文本并返回带置信度的结果

        参数:
            image: 输入图像(路径、PIL图像或numpy数组)

        返回:
            (识别文本, 带置信度的单词列表)
        """
        processed_img = self.preprocess_image(image)

        if self.config['ocr']['engine'] != 'tesseract':
            raise NotImplementedError("置信度分析目前仅支持Tesseract引擎")

        text, data = self._run_tesseract(processed_img)
        processed_text = self._postprocess_text(text, data)

        # 提取单词和置信度
        word_details = []
        n_boxes = len(data['level'])
        for i in range(n_boxes):
            if int(data['conf'][i]) > 0:  # 有效识别
                word_details.append({
                    'text': data['text'][i],
                    'confidence': int(data['conf'][i]),
                    'position': {
                        'left': data['left'][i],
                        'top': data['top'][i],
                        'width': data['width'][i],
                        'height': data['height'][i]
                    }
                })

        return processed_text, word_details

    def batch_recognize(self, image_paths: List[str], max_workers: int = 4) -> Dict[str, str]:
        """
        批量识别多张图像

        参数:
            image_paths: 图像路径列表
            max_workers: 最大线程数

        返回:
            {图像路径: 识别文本} 的字典
        """
        results = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_path = {
                executor.submit(self.recognize_text, path): path
                for path in image_paths
            }

            for future in concurrent.futures.as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    results[path] = future.result()
                except Exception as e:
                    results[path] = f"识别错误: {str(e)}"

        return results

    def _run_easyocr(self, image: Image.Image) -> str:
        """使用EasyOCR引擎识别文本"""
        try:
            import easyocr
        except ImportError:
            raise ImportError("请先安装easyocr: pip install easyocr")

        # 转换图像为numpy数组
        img_array = np.array(image)
        if len(img_array.shape) == 3 and img_array.shape[2] == 3:
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # 初始化reader
        langs = self.config['ocr']['lang'].split('+')
        reader = easyocr.Reader(langs)

        # 识别文本
        results = reader.readtext(img_array)
        text = '\n'.join([result[1] for result in results])

        return text

    def _run_paddleocr(self, image: Image.Image) -> str:
        """使用PaddleOCR引擎识别文本"""
        try:
            from paddleocr import PaddleOCR
        except ImportError:
            raise ImportError("请先安装paddleocr: pip install paddleocr")

        # 转换图像为numpy数组
        img_array = np.array(image)
        if len(img_array.shape) == 3 and img_array.shape[2] == 3:
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # 初始化OCR
        ocr = PaddleOCR(use_angle_cls=True, lang=self.config['ocr']['lang'])

        # 识别文本
        result = ocr.ocr(img_array, cls=True)
        text = '\n'.join([line[1][0] for line in result[0]])

        return text

    def visualize_ocr_results(self, image_path: str, output_path: str = None):
        """
        可视化OCR识别结果

        参数:
            image_path: 输入图像路径
            output_path: 输出图像路径(可选)
        """
        # 读取图像
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"无法读取图像: {image_path}")

        # 预处理图像
        pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        processed_image = self.preprocess_image(pil_image)
        cv_image = np.array(processed_image)
        if len(cv_image.shape) == 3 and cv_image.shape[2] == 3:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

        # 获取识别结果
        _, data = self._run_tesseract(processed_image)

        # 绘制边界框
        n_boxes = len(data['level'])
        for i in range(n_boxes):
            if int(data['conf'][i]) > self.config['postprocess']['confidence_threshold']:
                (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(cv_image, data['text'][i], (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # 显示或保存结果
        if output_path:
            cv2.imwrite(output_path, cv_image)
        else:
            plt.figure(figsize=(20, 20))
            plt.imshow(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()


def main():
    # 初始化OCR处理器
    ocr = OCRProcessor()

    # 设置Tesseract路径(如果需要)
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # 识别单张图像
    image_path = '图片.png'
    if os.path.exists(image_path):
        start_time = time.time()

        # 识别文本
        text = ocr.recognize_text(image_path)

        # 带置信度的识别
        # text, details = ocr.recognize_with_confidence(image_path)
        # print("识别细节:", details)

        elapsed = time.time() - start_time
        print(f"识别完成，耗时: {elapsed:.2f}秒")
        print("识别结果:")
        print(text)

        # 可视化结果
        ocr.visualize_ocr_results(image_path, 'output.png')
    else:
        print(f"图像文件不存在: {image_path}")


if __name__ == '__main__':
    main()