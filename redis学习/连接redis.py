# coding=gbk
import csv
import redis
rc=redis.Redis(host="172.16.32.122",port=6379,db=0)


# rc.set("k1","我爱你".encode("utf-8"))
# print(rc.get("k1").decode("utf-8"))
with open('icv.csv',"r",encoding='gbk') as fp:
    reader = csv.DictReader(fp)
    # print(reader)
    # for i in reader:
    #     print(i)
    for i in reader:
        rc.hset('user', 'name', i['name'].encode("utf-8"))
        print(rc.hget('user',"name").decode("utf-8"))

    # for fydw in reader:
    #     rc.sadd("court", fydw)
    #     time.sleep(0.5)

