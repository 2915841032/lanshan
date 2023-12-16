# coding=gbk
import redis

rc = redis.Redis(host="172.16.32.122", port=6379, db=0)
############################################key
# rc.set("k1","这是k1".encode("gbk"))
# print(rc.get("k1").decode("gbk"))
# print(rc.exists("k1"))
# rc.set("k2","yu")
# print(rc.delete("k2"))
# print(rc.flushdb())
############################################String
# rc.append("k2","ye")
# print(rc.get("k2").decode("gbk"))
# print(rc.strlen("k2"))
# rc.setnx("k4","5")
# print(rc.get("k4"))

# rc.incrby("k4",30)
# print(rc.get("k4"))
#
# rc.decrby("k4",30)
# print(rc.get("k4"))

# rc.set("yu","asdfghjklkjhgfdsa")
# print(rc.getrange("yu",0,5))
# print(rc.setrange("yu",5,"123"))
# print(rc.get("yu"))

# rc.setex("l",85,"yi")
# print(rc.ttl("l"))
# print(rc.getset("k4", "op"))
############################################list
rc.flushdb()
# rc.lpush("k1","a","b","c","e","f")
# rc.rpush("k2","a","b","c","e","f")
# rc.lpop("k1")
# # print(rc.lrange("k1", 0, -1))
# print(rc.llen("k1"))
# # print(rc.lindex("k2", 4))
# rc.linsert("k1","before","b","ty")
# print(rc.lrange("k1", 0, -1))
#
# rc.lrem("k1",2,"a")
# rc.lset("k1",2,"tu")
# print(rc.lrange("k1", 0, -1))




#
############################################Set
# rc.sadd("k1","q","w","e","r","t")
# print(rc.smembers("k1"))
# print(rc.sismember("k1", "e"))
# print(rc.scard("k1"))
# print(rc.srem("k1", "q"))
# print(rc.smembers("k1"))
# print(rc.spop("k1"))
# print(rc.smembers("k1"))
# print(rc.srandmember("k1", 7))
# rc.sadd("k2","e")
# rc.move("k1","k2")
# print(rc.sinter("k1", "k2"))
# print(rc.sunion("k1", "k2"))
# print(rc.sdiff("k1", "k2"))

############################################hash
# rc.hset("k1", "name", "jack")
# rc.hset("k1", "age", "jack")
# rc.hset("k1", "sex", "jack")
# rc.hset("k1", "2", "2")
# rc.hsetnx("k1", "ru", "2")
# print(rc.hget("k1", "name"))
# print(rc.hexists("k1", "name"))
# print(rc.hincrby("k1", "2", 2))
# print(rc.hkeys("k1"))
# print(rc.hvals("k1"))


############################################Hset
# rc.zadd("k1", {"name": 200, "age": 300, "sex": 520})
# print(rc.zrange("k1", 0, -1))
# print(rc.zrangebyscore("k1", 200, 300))
# print(rc.zrevrangebyscore("k1", 600, 300))
# print(rc.zincrby("k1", 500, "name"))
# print(rc.zrem("k1", "age"))
# print(rc.zcount("k1", 0, 700))
# print(rc.zrank("k1", "sex"))
