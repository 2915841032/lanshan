# -*- coding: utf-8 -*-
# @File : 25.uuid的创建.py
# @Author : 阿波
# @Time : 2023/9/4 20:11
# @Software: PyCharm
import uuid

# 生成一个UUID: 根据主机，序列号和当前时间。
print(uuid.uuid1(213213123))



my_uuid = uuid.uuid4()

# 将UUID转换为字节表示
uuid_bytes = my_uuid.bytes


# import uuid
#
uuid_bytes = b'\x6b\xa7\xb8\x10\x9d\xad\x11\xd1\x80\xb4\x00\xc0\x4f\xd4\x30\xc8'

# 从字节表示中还原UUID
my_uuid = uuid.UUID(bytes=uuid_bytes)
print(my_uuid)

