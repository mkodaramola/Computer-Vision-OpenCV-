import cv2
import mediapipe as mp
import pyautogui as pg
from time import sleep
import math
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
pg.FAILSAFE = False
scrW, scrH = pg.size()
x5 = 0
y5 = 0
x8 = 0
y8 = 0
x4 = 0
x1 =0
x12=0
c = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_height,frame_width, _ = frame.shape
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgbFrame)
    hands = output.multi_hand_landmarks

    if hands:        
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                if id == 4:
                    x4 = int(landmark.x*frame_width)

                    
                # if id == 17:
                #     x17 = int(landmark.x*frame_width)
                    
                    
                if id == 12:
                    x12 = int(landmark.x*frame_width)
                    # x17 = x17 if x17 > x1 else 100 
                        
                    # n = int(((x17-x1)/(x12-x8))*100)
                    # print(n)                   



                if id == 0:
                    x0 = int(landmark.x*frame_width)
                    
                    y0 = int(landmark.y*frame_height)
                    y0 = y0 - 200
                    #cv2.circle(img=frame, center=(int(x0),int(y0)),radius=20,color=(10,45,185))
                    mx = (x0/frame_width)*scrW
                    my = (y0/frame_height)*scrH
                    pg.moveTo(mx,my,0.1)


                if id == 8:
                    x8 = int(landmark.x*frame_width)
                    if (abs(x8 - x0)) < 120:
                        pg.click()
                        print("click")
                        sleep(1)
                        pass

                    c+=1


                print("x8",x8)
                    
                print("x0",x12)

                print(abs(x8-x12))


                               
                    
    cv2.imshow('Virtual Mouse',frame)
    if cv2.waitKey(1) == ord('q'):
        break