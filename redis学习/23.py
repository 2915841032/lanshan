#encoding=gbk
import redis
rc = redis.Redis(host="localhost", port=6379, db=0)
rc.set("k1","这是k1".encode("gbk"))
print(rc.get("k1").decode("gbk"))
print(rc.keys("*"))
print(rc.exists("k1"))