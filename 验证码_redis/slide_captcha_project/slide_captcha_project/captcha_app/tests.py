import cv2
import numpy as np
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import base64

# 创建会话对象，保持cookies
session = requests.Session()


def get_captcha():
    """获取验证码并保存到临时文件"""
    response = session.get("http://127.0.0.1:8000/get_captcha/")
    if response.status_code != 200:
        raise Exception("获取验证码失败")

    data = response.json()

    # 保存背景图
    bg_data = base64.b64decode(data['bg'])
    with open('images/captcha_bg.png', 'wb') as f:
        f.write(bg_data)

    # 保存滑块图
    slider_data = base64.b64decode(data['slider'])
    with open('images/captcha_slider.png', 'wb') as f:
        f.write(slider_data)

    return data['y'],data['captcha_id']


def identify_gap(bg, out):
    '''
    bg: 背景图片路径
    out: 输出图片路径
    返回值: 缺口左上角的X坐标
    '''
    # 读取背景图片
    img = cv2.imread(bg)
    if img is None:
        raise ValueError(f"无法读取图片: {bg}")

    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 问题修复：直接寻找暗色区域（缺口）
    # 白底上缺口是灰色（较暗区域）
    _, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

    # 形态学操作增强缺口特征
    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)

    # 查找轮廓
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 筛选可能的缺口轮廓
    gap_contour = None
    gap_size = 50
    min_size = int(gap_size * 0.8)  # 最小尺寸40
    max_size = int(gap_size * 1.2)  # 最大尺寸60

    for cnt in contours:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)

        # 面积过滤小噪点
        if area < 1000:
            continue

        # 检查尺寸是否接近50x50
        if (min_size < w < max_size and
                min_size < h < max_size and
                abs(w - h) < 10):  # 宽高差小于10像素

            # 检查宽高比
            ratio = w / float(h)
            if 0.8 < ratio < 1.2:  # 接近正方形
                gap_contour = cnt
                break

    # 如果找到符合条件的轮廓
    if gap_contour is not None:
        x, y, w, h = cv2.boundingRect(gap_contour)

        # 绘制矩形框标记缺口
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 保存结果
        cv2.imwrite(out, img)

        return x

    # 如果没找到轮廓，尝试替代方法
    # 计算梯度图
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    gradient = np.sqrt(grad_x ** 2 + grad_y ** 2)
    gradient = np.uint8(255 * gradient / np.max(gradient))

    # 二值化梯度图
    _, grad_thresh = cv2.threshold(gradient, 50, 255, cv2.THRESH_BINARY)

    # 查找轮廓
    contours, _ = cv2.findContours(grad_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 再次尝试查找合适的轮廓
    for cnt in contours:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)

        if (min_size < w < max_size and
                min_size < h < max_size and
                abs(w - h) < 15 and
                1000 < area < 5000):
            # 绘制矩形框标记缺口
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite(out, img)
            return x

    # 如果仍然没找到，保存调试信息
    cv2.imwrite("images/debug_gray.jpg", gray)
    cv2.imwrite("images/debug_thresh.jpg", thresh)
    cv2.imwrite("images/debug_morph.jpg", morph)
    cv2.imwrite("images/debug_gradient.jpg", gradient)
    cv2.imwrite("images/debug_grad_thresh.jpg", grad_thresh)
    cv2.imwrite(out, img)

    return 0  # 返回0表示未找到缺口


@csrf_exempt
def verify_captcha(request):
    """验证验证码（添加Redis支持）"""
    try:
        from django_redis import get_redis_connection
        redis_conn = get_redis_connection("default")
    except ImportError:
        redis_conn = None

    try:
        data = request.POST
        offset = int(data.get('offset', -1))

        # 优先使用Redis存储验证码位置
        if redis_conn:
            captcha_x = redis_conn.get('captcha_x')
            if captcha_x:
                captcha_x = int(captcha_x.decode())
        else:
            # 回退到session
            captcha_x = request.session.get('captcha_x', -1)

        if captcha_x == -1 or offset == -1:
            return JsonResponse({'success': False, 'msg': '参数错误'})

        # 允许误差5像素
        if abs(offset - captcha_x) < 5:
            return JsonResponse({'success': True, 'msg': '验证成功'})
        else:
            return JsonResponse({'success': False, 'msg': '验证失败'})
    except Exception as e:
        return JsonResponse({'success': False, 'msg': str(e)})


# 主流程
def main():
    # 如果没有文件夹就创建
    if not os.path.exists('images'):
        os.makedirs('images')

    # 1. 获取验证码
    y_pos,captcha_1 = get_captcha()
    print(f"滑块Y坐标: {y_pos}")

    # 2. 识别缺口位置
    gap_x = identify_gap('images/captcha_bg.png', 'images/result.png')
    print(f"识别到的缺口X坐标: {gap_x}")

    # 3. 验证验证码
    response = session.post(
        "http://127.0.0.1:8000/verify_captcha/",
        data={'offset': gap_x,'captcha_id': f'{captcha_1}'}
    )

    print(f"验证结果: {response.json()}")
    print(f"HTTP状态码: {response.status_code}")


if __name__ == "__main__":
    main()