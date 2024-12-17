import numpy as np
import cv2
import time
import pyttsx3

# Replace the video source with the ESP32-CAM stream URL
cap = cv2.VideoCapture("http://192.168.223.10/")

engine = pyttsx3.init()  # Initialize text-to-speech engine

while True:
    # Read two consecutive frames from the ESP32-CAM
    ret, frame1 = cap.read()
    if not ret:
        print("Failed to grab frame. Retrying...")
        continue
    
    frame1 = cv2.resize(frame1, (200, 250))
    frame1 = cv2.flip(frame1, 1)

    ret, frame2 = cap.read()
    if not ret:
        print("Failed to grab second frame. Retrying...")
        continue
    
    frame2 = cv2.resize(frame2, (400, 350))
    frame2 = cv2.flip(frame2, 1)

    # Compute the difference between the two frames
    diff = cv2.absdiff(frame1, frame2)

    # Process the difference to detect motion
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours in the binary image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 1000:
            continue  # Skip small movements
        
        # Alert user about detected motion
        engine.say("Motion detected!")
        engine.runAndWait()

        # Draw bounding box around the motion
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Display the video stream with motion detection
    cv2.imshow('ESP32-CAM Feed', frame1)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
