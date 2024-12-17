import cv2
import time
import random
img = cv2.imread('images/bot.jpg',1)
img = cv2.resize(img,(600,400))	

cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


#Copy Part of Image
# c = img[100:200,200:399]

# img[0:100,400:599] = c


#Change pixel Colour
# for i in range(img.shape[0]):
# 	for j in range(140):
# 		img[i][j] = [0,0,0]

# for i in range(img.shape[0]):
# 	for j in range(img.shape[1]-1,img.shape[1]-230,-1):
# 		img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

