import cv2
import time
import numpy as np
import handTrackingModule as HTM
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume





wcCam, hCam = 1280, 720


cap = cv2.VideoCapture(0)
#settinf the width and height of the camera
cap.set(3, wcCam)
cap.set(4, hCam)
prevTime = 0

detector = HTM.handDetector(detectionCon=0.7)#change conf so that detection is smoother

#initialize
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)


volRange=volume.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]







while True:
    success, img = cap.read()
    img = detector.findHands(img)
    LMList = detector.findPosition(img, draw=False)
    if len(LMList) != 0:
        #print(LMList[4], LMList[8])# tim of thumb and index finger

        x1,y1 = LMList[4][1], LMList[4][2]
        x2,y2 = LMList[8][1], LMList[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2 #center of the line
    
        cv2.circle(img, (x1,y1), 10, (7, 240, 81), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (7, 240, 81), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (127, 7, 240), 3)
        cv2.circle(img, (cx,cy), 10, (7, 240, 104), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1) #length of the line
        print(length)

        #set the range of the volume
        volume_percentage = np.interp(length, [50, 380], [minVol, maxVol])
        volume.SetMasterVolumeLevel(volume_percentage, None)

        if length < 50:
            cv2.circle(img, (cx,cy), 10, (255,255,255), cv2.FILLED)
      



    currentTime=time.time()
    fps = 1/(currentTime-prevTime)
    prevTime = currentTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
            break
    
cap.release()
cv2.destroyAllWindows()
