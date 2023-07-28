import cv2
from matplotlib import image 

# Create a video capture object, in this case we are reading the video from a file
vid_capture = cv2.VideoCapture('../Videos/fiba video.mp4')

if (vid_capture.isOpened() == False):
	print("Error opening the video file")
# Read fps and frame count
else:
	# Get frame rate information
	# You can replace 5 with CAP_PROP_FPS as well, they are enumerations
	fps = vid_capture.get(5)
	print('Frames per second : ', fps,'FPS')

	# Get frame count
	# You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
	frame_count = vid_capture.get(7)
	print('Frame count : ', frame_count)
ret,frame=vid_capture.read()
print("frame==",frame)
image_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
print("image=",type(image_bytes),len(image_bytes))
# while vid_capture.isOpened():
# 	ret, frame = vid_capture.read()
#     print("frame=",frame)
# 	if ret == True:
# 		cv2.imshow('Frame',frame)
# 		# 20 is in milliseconds, try to increase the value, say 50 and observe
# 		key = cv2.waitKey(20)
		
# 		if key == ord('q'):
# 			break
# 	else:
# 		break

# Release the video capture object
# vid_capture.release()
# cv2.destroyAllWindows()
