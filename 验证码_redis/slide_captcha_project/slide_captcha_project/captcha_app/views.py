import json
import random
import io
import os
import uuid
from PIL import Image, ImageDraw
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
import redis  # 添加Redis支持

# 初始化Redis连接
REDIS_PASSWORD = "root"  # 您的Redis密码
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

try:
    redis_conn = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
    # 测试连接
    redis_conn.ping()
except redis.ConnectionError:
    redis_conn = None
    print("警告: 无法连接到Redis服务器，将使用内存缓存")


# 生成滑块和带缺口的背景图
class SlideCaptcha:
    def __init__(self, width=300, height=150, block_size=50):
        self.width = width
        self.height = height
        self.block_size = block_size

        # 从Redis获取配置（如果可用）
        if redis_conn:
            # 尝试获取自定义配置
            redis_width = redis_conn.get("captcha:width")
            redis_height = redis_conn.get("captcha:height")
            redis_block_size = redis_conn.get("captcha:block_size")

            if redis_width:
                self.width = int(redis_width)
            if redis_height:
                self.height = int(redis_height)
            if redis_block_size:
                self.block_size = int(redis_block_size)

    def create_captcha(self):
        # 检查Redis中是否有自定义背景目录
        custom_dir = None
        if redis_conn:
            custom_dir = redis_conn.get("captcha:image_dir")

        image_dir = custom_dir or os.path.join(settings.BASE_DIR, 'captcha_app', 'static', 'images')

        try:
            image_files = [f for f in os.listdir(image_dir) if f.endswith(('jpg', 'png', 'jpeg'))]
            if not image_files:
                raise FileNotFoundError
            random_image_path = os.path.join(image_dir, random.choice(image_files))
            bg = Image.open(random_image_path).convert('RGB')
            bg = bg.resize((self.width, self.height))
        except (FileNotFoundError, NotADirectoryError):
            # Fallback to generated image if no images found
            bg = Image.new('RGB', (self.width, self.height), (255, 255, 255))
            draw = ImageDraw.Draw(bg)
            for _ in range(5):
                start = (random.randint(0, self.width), random.randint(0, self.height))
                end = (random.randint(0, self.width), random.randint(0, self.height))
                draw.line([start, end],
                          fill=(random.randint(100, 200), random.randint(100, 200), random.randint(100, 200)), width=2)

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

    # 生成唯一验证码ID
    captcha_id = str(uuid.uuid4())

    # 保存到Redis (过期时间5分钟)
    if redis_conn:
        redis_conn.setex(f"captcha:{captcha_id}", 300, x)
    else:
        # Redis不可用时使用session
        request.session[f'captcha_{captcha_id}'] = x

    # 返回图片base64
    import base64
    bg_base64 = base64.b64encode(bg_bytes.read()).decode()
    slider_base64 = base64.b64encode(slider_bytes.read()).decode()

    return JsonResponse({
        'bg': bg_base64,
        'slider': slider_base64,
        'y': y,
        'captcha_id': captcha_id
    })


@csrf_exempt
def verify_captcha(request):
    try:
        # 检查请求头是否为JSON
        if request.content_type == 'application/json':
            # 解析JSON数据
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                data = {}
        else:
            data = request.POST
            print(data)
        offset = int(data.get('offset', -1))
        captcha_id = data.get('captcha_id', '')

        if not captcha_id:
            return JsonResponse({'success': False, 'msg': '缺少验证码ID'})

        # 从Redis获取验证码位置
        if redis_conn:
            x = redis_conn.get(f"captcha:{captcha_id}")
            if x is None:
                return JsonResponse({'success': False, 'msg': '验证码已过期'})
            x = int(x)
        else:
            # Redis不可用时使用session
            x = request.session.get(f'captcha_{captcha_id}', -1)
            if x == -1:
                return JsonResponse({'success': False, 'msg': '验证码已过期'})

        # 允许误差5像素
        if abs(offset - x) < 5:
            # 验证成功后删除验证码
            if redis_conn:
                redis_conn.delete(f"captcha:{captcha_id}")
            else:
                if f'captcha_{captcha_id}' in request.session:
                    del request.session[f'captcha_{captcha_id}']

            return JsonResponse({
                'success': True,
                'msg': '验证成功',
                'data': [{'x': x, 'offset': offset}]
            })
        else:
            return JsonResponse({
                'success': False,
                'msg': f'验证失败，预期位置: {x}，实际位置: {offset}'
            })
    except Exception as e:
        return JsonResponse({'success': False, 'msg': str(e)})


# 首页视图
def index(request):
    return render(request, 'captcha_app/index.html')