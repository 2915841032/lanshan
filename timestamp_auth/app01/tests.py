from django.test import TestCase

# Create your tests here.
# 生成带校验位的时间戳
from utils import generate_timestamp_with_check

timestamp_with_check = generate_timestamp_with_check()
print("Generated Timestamp with Check:", timestamp_with_check)

# 示例请求
# 假设你有一个Django开发服务器在 localhost:8000 运行
import requests

response = requests.get("http://localhost:8000/api/validate-timestamp/", params={"timestamp": timestamp_with_check})
print(response.json())
