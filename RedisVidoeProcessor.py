import time
import cv2
import redishelper
redisCon=redishelper.getRedisInstance()
Stream=cv2.VideoCapture("rtsp://admin:12345678a@192.168.1.2")
while True:
    # Readvideo=redisCon.get('LON').decode()
    Readvideo=True
    if Readvideo:
        frame=Stream.read()
        image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        redisCon.xadd('Images',{'image':image_bytes})
    time.sleep(10)


