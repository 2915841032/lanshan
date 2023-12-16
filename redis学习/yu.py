import redis

rc=redis.Redis(host='172.16.32.122',port=6379,db=0)

rc.flushdb()
