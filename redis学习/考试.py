#encoding=gbk
import redis
rc = redis.Redis(host="192.168.3.66", port=6379, db=0)
rc.sadd("set_37","swxx_1","swxx_2","swxx_3","swxx_3","swxx_4","swxx_5")
print("创建集合成功")
print(rc.smembers("set_37"))
print("随机打印一个值\n")
hnsw=rc.spop("set_37")
print(hnsw)
# 学号:37