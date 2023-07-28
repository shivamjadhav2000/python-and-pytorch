import redis
redisdb6=redis.ConnectionPool(
    host="localhost",
    db=6,
    port=6379
)
def getRedisInstance():
    return redis.StrictRedis(connection_pool=redisdb6)