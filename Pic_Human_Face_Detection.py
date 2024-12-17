import numpy as np
import cv2


#cap = cv2.VideoCapture(0)
pic = 'i7.jpg'
cap = cv2.imread(pic,0)
frame2 = cv2.imread(pic,1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
rv = []
avfe = None
def av(x):
	s = 0
	for i in x:
		s+=i
	return s/len(x)


	
cap = cv2.imread(pic,0)
frame2 = cv2.imread(pic,1)
frame = cv2.resize(cap,(400,350))
frame2 = cv2.resize(frame2,(400,350))



faces = face_cascade.detectMultiScale(frame,1.3,5)
print(len(faces))
for (x,y,w,h) in faces:
	cv2.rectangle(frame2,(x,y),(x+w,y+h),(255,0,0),2)
	ff_gray = frame[y:y+w,x:x+w]
	ff_color = frame2[y:y+w,x:x+w]
	eyes = eye_cascade.detectMultiScale(ff_gray,1.3,5)
	
	if len(eyes) == 2:
		average_eyeWidth = (eyes[0][2]+eyes[1][2])/2
		average_eyeHeight = (eyes[0][3]+eyes[1][3])/2
		eyeDistance = abs(eyes[1][0]-eyes[0][0])
		faceWidth = faces[0][2]
		faceHeight = faces[0][3]
		if (eyeDistance == 0):
			eyeDistance = 1
		face_eye = (faceWidth*0.8)/(eyeDistance)
		# print("Face Width:",faceWidth)
		# print("Face Height:",faceHeight)
		# print("Eyes Width:",average_eyeWidth)
		# print("Eyes Height:",average_eyeHeight)
		# print("Distance btw eyes:",eyeDistance)
		
		if len(rv) > 30:
			avfe = av(rv)
			rv.clear()

		rv.append(face_eye)
		print("Face to Eye Ratio:",avfe)


		print("------------------")
	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(ff_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		#print("ex:",ex,"\ney:",ey)

	
cv2.imshow('Face Detection',frame2)


cv2.waitKey()

cv2.destroyAllWindows()
