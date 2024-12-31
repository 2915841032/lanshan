import random
import string
import io
from django.shortcuts import render
from django.http import HttpResponse
from django_redis import get_redis_connection
from PIL import Image, ImageDraw, ImageFont


# 生成随机验证码
def generate_verification_code():
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


# 生成验证码图片
def generate_image(code):
	# 创建一个新的白色背景图片，尺寸为 80x80
	image = Image.new('RGB', (80, 40), color=(255, 255, 255))

	# 获取绘制对象
	draw = ImageDraw.Draw(image)

	# 加载自定义字体，并设置字体大小
	try:
		# 使用系统字体，或者指定你自己的字体文件路径
		font = ImageFont.truetype("arial.ttf", 13)  # 设置字体大小为40
	except IOError:
		# 如果找不到指定的字体文件，使用默认字体
		font = ImageFont.load_default()

	# 在图片上绘制验证码文本
	text_width, text_height = draw.textsize(code, font=font)
	position = ((80 - text_width) // 2, (40 - text_height) // 2)  # 居中显示
	draw.text(position, code, font=font, fill=(0, 0, 0))  # 黑色字体

	return image

# 保存验证码到Redis
def save_code_to_redis(code, request):
	redis_conn = get_redis_connection("default")
	redis_conn.setex(f"captcha:{request.session.session_key}", 300, code)  # 5分钟有效期


# 图片验证码视图
def captcha(request):
	code = generate_verification_code()
	image = generate_image(code)

	# 将验证码保存到Redis
	save_code_to_redis(code, request)

	# 将图片输出为HttpResponse
	response = HttpResponse(content_type="image/png")
	image.save(response, "PNG")
	return response


# 验证用户输入的验证码
def verify_captcha(request):
	user_input = request.POST.get("captcha")
	redis_conn = get_redis_connection("default")
	stored_code = redis_conn.get(f"captcha:{request.session.session_key}")

	if stored_code and stored_code.decode('utf-8') == user_input.upper():
		return HttpResponse("验证码验证通过")
	else:
		return HttpResponse("验证码错误", status=400)

def index(request):
	return render(request, 'index.html')