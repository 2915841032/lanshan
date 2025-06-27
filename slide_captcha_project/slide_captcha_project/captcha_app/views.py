import random
import io
import os
from PIL import Image, ImageDraw, ImageFilter
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings

# 生成滑块和带缺口的背景图
class SlideCaptcha:
    def __init__(self, width=300, height=150, block_size=50):
        self.width = width
        self.height = height
        self.block_size = block_size

    def create_captcha(self):
        image_dir = os.path.join(settings.BASE_DIR, 'captcha_app', 'static', 'images')
        try:
            image_files = [f for f in os.listdir(image_dir) if f.endswith(('jpg', 'png', 'jpeg'))]
            if not image_files:
                raise FileNotFoundError
            random_image_path = os.path.join(image_dir, random.choice(image_files))
            bg = Image.open(random_image_path).convert('RGB')
            bg = bg.resize((self.width, self.height))
        except FileNotFoundError:
            # Fallback to generated image if no images found
            bg = Image.new('RGB', (self.width, self.height), (255, 255, 255))
            draw = ImageDraw.Draw(bg)
            for _ in range(5):
                start = (random.randint(0, self.width), random.randint(0, self.height))
                end = (random.randint(0, self.width), random.randint(0, self.height))
                draw.line([start, end], fill=(random.randint(100, 200), random.randint(100, 200), random.randint(100, 200)), width=2)

        # 随机生成滑块位置
        x = random.randint(self.block_size + 10, self.width - self.block_size - 10)
        y = random.randint(10, self.height - self.block_size - 10)

        # 生成滑块形状（简单方块）
        block = Image.new('RGB', (self.block_size, self.block_size), (0, 0, 0))
        block_draw = ImageDraw.Draw(block)
        block_draw.rectangle([0, 0, self.block_size, self.block_size], fill=(150, 150, 150))

        # 在背景图上挖出滑块形状
        mask = Image.new('L', (self.block_size, self.block_size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rectangle([0, 0, self.block_size, self.block_size], fill=255)

        bg_with_hole = bg.copy()
        bg_with_hole.paste((180, 180, 180), (x, y, x + self.block_size, y + self.block_size), mask)

        # 滑块图像
        slider = bg.crop((x, y, x + self.block_size, y + self.block_size))

        # 转换为bytes
        bg_bytes = io.BytesIO()
        bg_with_hole.save(bg_bytes, format='PNG')
        bg_bytes.seek(0)

        slider_bytes = io.BytesIO()
        slider.save(slider_bytes, format='PNG')
        slider_bytes.seek(0)

        return bg_bytes, slider_bytes, x, y

@csrf_exempt
def get_captcha(request):
    captcha = SlideCaptcha()
    bg_bytes, slider_bytes, x, y = captcha.create_captcha()
    # 保存x到session用于验证
    request.session['captcha_x'] = x

    # 返回图片base64
    import base64
    bg_base64 = base64.b64encode(bg_bytes.read()).decode()
    slider_base64 = base64.b64encode(slider_bytes.read()).decode()

    return JsonResponse({'bg': bg_base64, 'slider': slider_base64, 'y': y})

@csrf_exempt
def verify_captcha(request):
    try:
        data = request.POST
        offset = int(data.get('offset', -1))
        x = request.session.get('captcha_x', -1)
        if x == -1 or offset == -1:
            return JsonResponse({'success': False, 'msg': '参数错误'})
        # 允许误差5像素
        if abs(offset - x) < 5:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'msg': '验证失败'})
    except Exception as e:
        return JsonResponse({'success': False, 'msg': str(e)})

# 首页视图

def index(request):
    return render(request, 'captcha_app/index.html')