import base64
import hashlib
from pyDes import *
import time
import json

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class My_AES_CBC():
    def __init__(self, key, iv):
        # key 和 iv 必须为 16 位
        self.key = key
        self.mode = AES.MODE_CBC
        self.cryptor = AES.new(self.key, self.mode, iv)

    def encrypt(self, plain_text):
        encode_text = plain_text.encode('utf-8')
        pad_text = pad(encode_text, AES.block_size)
        encrypted_text = self.cryptor.encrypt(pad_text)
        # base64_text = base64.b32encode(encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        plain_text = self.cryptor.decrypt(encrypted_text)
        plain_text = unpad(plain_text, AES.block_size).decode()
        return plain_text


Aes_key = '9B8FD68A366F4D03'.encode()
Aes_IV = '305FB72D83134CA0'.encode('utf-8')
    
    
def getActiveCode(machine_code):
    encrypt_code = My_AES_CBC(Aes_key, Aes_IV).encrypt(machine_code)
    active_code = hashlib.md5(encrypt_code).hexdigest().upper()
    return active_code

def getTimeLimitedCode(machine_code, ts):
    active_code = getActiveCode(machine_code)
    data = {
        "code": active_code,
        "endTs": ts,
    }
    text = json.dumps(data);
    
    encrypt_code = My_AES_CBC(Aes_key, Aes_IV).encrypt(text)
    active_code = base64.b32encode(encrypt_code)
    return active_code.decode()
    
if __name__ == '__main__':
    machine_code = input('请输入机器码:')
    str_time = input('请输入到期时间，格式如：2023-05-20 12:00:00 \n')
    
    time_array = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')
    timestamp = int(time.mktime(time_array))

    active_code = getTimeLimitedCode(machine_code, timestamp)
    
    print('限时激活码:', active_code)

    input('Press Enter to exit…')