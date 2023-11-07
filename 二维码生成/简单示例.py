import qrcode

# 定义二维码内容
data = 'https://www.baidu.com'

# 生成二维码图像
img = qrcode.make(data)

# 保存二维码图像
img.save('qrcode.png')




from PIL import Image


# 定义二维码内容
data = 'https://www.baidu.com'

# 生成二维码图像
img = qrcode.make(data)

# 加载背景图像
bg = Image.open('1.jpg')

# 调整背景图像大小
bg = bg.resize(img.size)

# 合并二维码和背景
img_bg = Image.alpha_composite(bg.convert('RGBA'), img.convert('RGBA'))

# 保存二维码图像
img_bg.save('qrcode_bg.png')