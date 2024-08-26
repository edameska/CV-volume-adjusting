import cv2
import mediapipe as mp

import time #check frame rate

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConf = detectionCon
        self.trackConf = trackCon

        self.mpHands = mp.solutions.hands # hands module
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode, 
            max_num_hands=self.maxHands, 
            min_detection_confidence=self.detectionConf, 
            min_tracking_confidence=self.trackConf
            )
        self.mpDraw = mp.solutions.drawing_utils # drawing module

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB because hands use only RGB
        self.results = self.hands.process(imgRGB)  # Assign to self.results here
        if self.results.multi_hand_landmarks:
            for handLandmarks in self.results.multi_hand_landmarks:  # Extract info from each hand
                if draw:
                    self.mpDraw.draw_landmarks(img, handLandmarks, self.mpHands.HAND_CONNECTIONS)  # Draw the landmarks
        return img

    
    def findPosition(self, img, handNo=0, draw=True):
        landMList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lMark in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lMark.x*w), int(lMark.y*h)
                landMList.append([id, cx, cy])
        return landMList


def main():
    prevTime = 0
    currentTime=0
    cap = cv2.VideoCapture(0)# use default camera
    detector = handDetector()

    while True:
        success, img = cap.read() # read the image from the camera
        img = detector.findHands(img)
        landMList = detector.findPosition(img)
        if len(landMList) != 0:
            print(landMList[4])

        currentTime = time.time()
        fps = 1/(currentTime-prevTime)
        prevTime = currentTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 255, 204), 3) # put the frame rate on the image

        cv2.imshow("Image", img) # show the image
        cv2.waitKey(1) # wait for 1 milisecond


if __name__ == "__main__":
    main()