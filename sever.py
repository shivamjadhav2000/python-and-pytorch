import redis
db9=redis.ConnectionPool(host="localhost",port=6379,db=9)
redisCon=redis.StrictRedis(connection_pool=db9)
import time
i=0
while True:
  i=i+1
  redisCon.rpush('lll',{"i":i})
  time.sleep(1)
