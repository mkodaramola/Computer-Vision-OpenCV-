import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

ret, temp = cap.read()
k = 0

def HW(x):
    q = []
    i = 0
    for face in x:
        q.append([face[2], i])
        i += 1

    q.sort(reverse=True)
    return q[0][1]


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 350))
    frame = cv2.flip(frame, 1)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(faces) > 0:
        hi = HW(faces)
        temp = cv2.resize(temp, (faces[hi][2] + 5, faces[hi][3] + 5))
        print(hi)

    h, w = temp.shape[:2]  # Assign height and width values to h and w

    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_temp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)  # Convert temp to grayscale

    res = cv2.matchTemplate(gray, gray_temp, cv2.TM_CCOEFF)  # Use the grayscale images for matching
    minV, maxV, minL, maxL = cv2.minMaxLoc(res)
    location = maxL
    bott_r = (location[0] + w, location[1] + h)
    cv2.rectangle(frame, location, bott_r, (0, 255, 255), 2)

    cv2.imshow('Normal', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
