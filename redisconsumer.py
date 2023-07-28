import redishelper
import time
from datetime import datetime as dt
redisConn=redishelper.getRedisInstance()
if not redisConn.xinfo_groups('mystream'):
        redisConn.xgroup_create('mystream','appData')
while True:
    print("\n \n",dt.now())
    entires=redisConn.xreadgroup('appData',
                        'cons1',
                        {'mystream':'>'},
                        count=10,
                        block=2000
                        )
    print(entires,)
    print("\n \n",dt.now())
    time.sleep(1)
