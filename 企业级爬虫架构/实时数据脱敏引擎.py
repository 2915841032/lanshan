# 基于FPE格式保留加密
from pycryptodomex import Cipher
from fpe_util import FF3Cipher

class DataAnonymizer:
    def __init__(self, keys):
        self.fpe_cipher = FF3Cipher(keys)

    def process(self, record):
        # 对标识字段进行加密脱敏
        if'user_id'in record:
            record['user_id'] = self.fpe_cipher.encrypt(record['user_id'])
        # 对敏感字段进行泛化处理
        if'location'in record:
            record['location'] = self._generalize_gps(
                record['latitude'],
                record['longitude']
            )
        return record

    def _generalize_gps(self, lat, lon, precision=500):
        # 将GPS精度降低到500米范围
        return f"{round(lat, 3)},{round(lon, 3)}"