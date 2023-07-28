import redis
import numpy as np
import cv2
import cv2

im = cv2.imread('../Pictures/index.jpeg')
p1=redis.ConnectionPool(host = 'localhost',
                    port = 6379,
                    db = 6,
                    )
redisConn=redis.StrictRedis(connection_pool=p1)
k=np.array([[1,2,3,4],[5,6,7,8],[8,7,60,9]])
data={"image":str(im)}
redisConn.xadd('images',data)
entries=redisConn.xread({'images':'0'},block=5000)
for streamEntries in entries:
    for msg in streamEntries[1]:
        streamId=msg[0]
        data=msg[1]
        image=data[b'image'].decode()
        print("streamid=",streamId,image)
        print(type(image))
        k=np.fromstring(image,dtype=int,sep='')

print("k====",k)