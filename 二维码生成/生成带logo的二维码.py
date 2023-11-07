import qrcode
from PIL import Image
# 定义二维码内容
data = '我爱你啊'

# 生成二维码图像
img = qrcode.make(data)

# # 加载logo图像
# logo = Image.open('1.jpg')
#
# # 计算logo的大小
# w, h = img.size
# logo_w = int(w / 4)
# logo_h = int(h / 4)
#
# # 调整logo的大小
# logo = logo.resize((logo_w, logo_h))
#
# # 计算logo的位置
# pos = ((w - logo_w) // 2, (h - logo_h) // 2)
#
# # 合并二维码和logo
# img.paste(logo, pos)

# 保存二维码图像
img.save('qrcode_logo1.png')