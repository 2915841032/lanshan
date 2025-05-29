# 基于Redis的同意状态实时验证
import redis
from gdpr_consent import ConsentValidator


class ConsentMiddleware:
    def __init__(self):
        self.redis = redis.StrictRedis(host = 'gdpr-redis' , port = 6379 , db = 0)
        self.validator = ConsentValidator()

    def check_consent(self , user_id , data_type):
        consent_key = f"consent:{user_id}:{data_type}"
        # 检查实时同意状态
        if self.redis.get(consent_key) != b'1':
            return False
        # 验证同意有效期
        return self.validator.validate_signature(
            self.redis.hget(f"consent_meta:{user_id}" , "signature")
        )
