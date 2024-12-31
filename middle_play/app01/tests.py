from django.test import TestCase

import requests


headers = {
    "X-Auth-Token": "my_secret_token"
}
url = "http://127.0.0.1:8008/"
response = requests.get(url, headers=headers)

print(response.text)
print(response)
