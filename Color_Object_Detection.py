import numpy as np
import cv2


fr = cv2.VideoCapture(0)

temp = cv2.imread('images/blue.jpg',0)
while True:
	
	ret, cap = fr.read()
	cap = cv2.resize(cap,(800,650))
	cap = cv2.flip(cap,1)

	hsv = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)	#white-> blue, blue -> white
	lower_blue = np.array([94,80,2])
	upper_blue = np.array([126,255,255])
	blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)
	OnlyBlue = cv2.bitwise_and(cap,cap,mask=blue_mask)
	

	h,w = temp.shape
	methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
	
	gray = cv2.cvtColor(OnlyBlue,cv2.COLOR_BGR2GRAY)

	

	
	res = cv2.matchTemplate(gray,temp,cv2.TM_CCORR)
	print(cv2.TM_CCORR)
	minV, maxV, minL, maxL = cv2.minMaxLoc(res)
	location = maxL
	bott_r = (location[0]+w,location[1]+h)
	cv2.rectangle(cap, location,bott_r,(0,255,255),2)
	cv2.putText(cap,f"Blue Obj Conf: {maxV/10000000}",location,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),1)

	

	

	cv2.imshow('Normal',cap)

	#cv2.imshow('OnlyBlue',OnlyBlue)

	if cv2.waitKey(1) == ord('q'):
		break

fr.release()
cv2.destroyAllWindows()

# methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
# for methods in methods:
# 	res = cv2.matchTemplate(OnlyBlue,temp,method)
# 	minV, maxV, minL, maxL = cv2.minMaxLoc(res)
# 	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
# 		location = minL
# 	else:
# 		location = maxL
# 	bott_r = (location[0]+w,location[1]+h)
# 	cv2.rectangle(cap, location,bott_r,(0,255,255),2)