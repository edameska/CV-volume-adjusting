import cv2
import mediapipe as mp

import time #check frame rate

cap = cv2.VideoCapture(0)# use default camera

mpHands = mp.solutions.hands # hands module
hands = mpHands.Hands() # hands object with default parameters
mpDraw = mp.solutions.drawing_utils # drawing module

prevTime = 0
currentTime=0

while True:
    success, img = cap.read() # read the image from the camera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to RGB cuz hands uses only rgb
    res = hands.process(imgRGB)
    #print(res.multi_hand_landmarks) # print the landmarks
    if res.multi_hand_landmarks:
        for handLandmarks in res.multi_hand_landmarks: #extract info from each hand
           for id, lMark in enumerate(handLandmarks.landmark): # extract info from each landmark
                #get the height, width and channel of the image
                h, w, c = img.shape
                cx, cy = int(lMark.x*w), int(lMark.y*h) # get the x and y coordinates of the landmarks
                #if id == 0: #first landmark
                     #cv2.circle(img, (cx, cy), 15, (200, 255, 0), cv2.FILLED)
           mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS) # draw the landmarks
    
    currentTime = time.time()
    fps = 1/(currentTime-prevTime)
    prevTime = currentTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 204), 3) # put the frame rate on the image

    cv2.imshow("Image", img) # show the image
    cv2.waitKey(1) # wait for 1 milisecond
