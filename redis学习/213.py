#encoding=gbk
import redis
rc = redis.Redis(host="192.168.3.66", port=6379, db=0)

rc.rpush("set_27","swxx_1","swxx_2","swxx_3","swxx_4","swxx_5")
print("创建成功")

hnsw=rc.lpop("set_27")
print("成功")

rc.set("result_27",hnsw)
print(rc.get("result_27"))
print("设置成功")
