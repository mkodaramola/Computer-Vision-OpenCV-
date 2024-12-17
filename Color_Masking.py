import numpy as np
import cv2


fr = cv2.VideoCapture(0)

while True:
	ret, cap = fr.read()
	cap = cv2.resize(cap,(400,350))
	# width = int(cap.get(3))
	# height = int(cap.get(4))
	

	hsv = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)	#white-> blue, blue -> white

	lower_red = np.array([161,155,84])
	upper_red = np.array([179,255,255])

	lower_blue = np.array([94,80,2])
	upper_blue = np.array([126,255,255])

	lower_green = np.array([25,52,72])
	upper_green = np.array([102,255,255])

	lower_NoWhite = np.array([20,42,20])
	upper_NoWhite = np.array([179,255,255])

	NoWhite_mask = cv2.inRange(hsv,lower_NoWhite, upper_NoWhite)
	NoWhite = cv2.bitwise_and(cap,cap, mask=NoWhite_mask)


	red_mask = cv2.inRange(hsv,lower_red, upper_red)
	OnlyRed = cv2.bitwise_and(cap,cap, mask=red_mask)

	blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)
	OnlyBlue = cv2.bitwise_and(cap,cap,mask=blue_mask)

	green_mask = cv2.inRange(hsv,lower_green, upper_green)
	OnlyGreen = cv2.bitwise_and(cap,cap, mask=green_mask)

	cv2.imshow('Normal',cap)
	#cv2.imshow('OnlyRed',OnlyRed)
	cv2.imshow('OnlyGreen',OnlyGreen)
	#cv2.imshow('OnlyBlue',OnlyBlue)
	#cv2.imshow('No White',NoWhite)
	if cv2.waitKey(1) == ord('q'):
		break
# cap.release()
cv2.destroyAllWindows()




#--- Multiple Image in a Frame

# width = int(cap.get(3))
# height = int(cap.get(4))
# image = np.zeros(frame.shape,np.uint8)
# sf = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
# image[:height//2,:width//2] = cv2.rotate(sf,cv2.ROTATE_180)
# image[height//2:height,:width//2] = sf
# image[:height//2,width//2:width] = sf
# image[height//2:height,width//2:width] = sf



#--- Drawing Lines, Rectangle, Circle & Text

# img = cv2.line(frame, (50,50), (550,50),(255,255,255),2)
# img = cv2.rectangle(img,(100,150),(200,250),(0,255,255),2)
# img = cv2.circle(img,(305,170),100,(255,0,0),-1)
# img = cv2.putText(img, 'Jesus is Lord over all!', (200, height-10), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255),2,cv2.LINE_AA)



# lower_blue = np.array([90,50,50])
# upper_blue = np.array([130,255,255])