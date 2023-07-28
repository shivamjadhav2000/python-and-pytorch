import redishelper
redisCon=redishelper.getRedisInstance()
import time
import datetime as dt
T=1662192273
i=0
l=[{
    'fuellevel':433.8,
    'speed':2,
    'id':1
},
{
    'fuellevel':433.8,
    'speed':0.1,
        'id':2

},
{
    'fuellevel':433.7,
    'speed':2,
        'id':3

},
{
    'fuellevel':433.6,
    'speed':2,
        'id':4

},
{
    'fuellevel':433.5,
    'speed':2,
        'id':5

},
{
    'fuellevel':433.5,
    'speed':2,
        'id':6

},
{
    'fuellevel':437.9,
    'speed':2,
        'id':7

},
{
    'fuellevel':433.5,
    'speed':2,
        'id':8

},
{
    'fuellevel':433.4,
    'speed':2,
        'id':9

},
{
    'fuellevel':433.4,
    'speed':2,
        'id':10

}]
for i in l:
    t=int(time.time())
    i['time']=str(dt.datetime.now())
    print('t===',T)
    redisCon.xadd('mystream',i,id='*')
    T+=11
    time.sleep(2)