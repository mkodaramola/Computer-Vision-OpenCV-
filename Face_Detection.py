import numpy as np
import cv2
import random

def HW(x):
	q = []
	i = 0
	for face in x:
		q.append([face[2],i])
		i+=1


	q.sort(reverse=True)
	return q[0][1]



pic = 'images/i7.jpg'
cap = cv2.imread(pic,0)
cCap = cv2.imread(pic,1)
temp = cv2.imread('me.png',0)

# ret, frame = cap.read()
frame = cv2.resize(cap,(400,350))
cFrame = cv2.resize(cCap,(400,350))



#Detect Human Face in Image
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
faces = face_cascade.detectMultiScale(frame,1.3,5)

#Use Dimension of located Human face to resize temp

# if len(faces) > 0:
# 		hi = HW(faces)
# 		temp = cv2.resize(temp,(faces[0][2]+5,faces[0][3]+5))
# 		print(hi)

h,w = frame.shape







frame2 = frame.copy()
methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
for method in methods:
	res = cv2.matchTemplate(frame2,temp,method)
	minV, maxV, minL, maxL = cv2.minMaxLoc(res)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location = minL
	else:
		location = maxL
	bott_r = (location[0]+w,location[1]+h)
	cv2.rectangle(cFrame, location,bott_r,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
	cv2.imshow('Normal',cFrame)
	cv2.waitKey(0)
	cv2.destroyAllWindows()





# cv2.imshow('OnlyBlue',OnlyBlue)



# methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]
# for methods in methods:
# 	res = cv2.matchTemplate(OnlyBlue,temp,method)
# 	minV, maxV, minL, maxL = cv2.minMaxLoc(res)
# 	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
# 		location = minL
# 	else:
# 		location = maxL
# 	bott_r = (location[0]+w,location[1]+h)
# 	cv2.rectangle(frame, location,bott_r,(0,255,255),2)