#INITIAL SETUP
#----------------------------------------------------------------
from logging import captureWarnings
import cv2
import os
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import time 
import random
folderpath='C:\Users\KIIT\Desktop\python\CookieCutter-main'
myList=os.listdir(folderpath)
graphic=[cv2.imread(f'(folderpath)/(impath)')]  
for impath in myList:
    intro = graphic[1];
    kill =graphic[2];
    winner =graphic[3];
    cam =cv2.VideoCapture(0)
    detector=HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
sqr_img = cv2.imread('sqr(2).png') # read img\sqr (1) in the sqr_img variable
mlsa = cv2.imread('mlsa.png') # read img\mlsa in the mlsa variable
cv2.waitKey(1) #INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
gameOver = False
NotWon =True



cv2.imshow('squid Game',cv2.resize(intro,(0,0),fx=0.69,fy=0.69))
cv2.waitKey(1)


while True:
    cv2.imshow('squidgame',cv2.resize(intro(0,0),fx=0.69,fy=0.69))
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

TIMER_Max=45
Timer=TIMER_Max
maxMove=6500000
font=cv2.FONT_HERSHEY_COMPLEX_SMALL 

blank = np.zeros((500,500,3), dtype='uint8')


cv2.circle(sqr_img, (250,250), 50, (0,0,255), thickness=5)
## iamge to draw on, centre pts, radius, color(RGB), border



while True:
    isTrue, frame = cam.read()
    hands, img = detector.findHands(frame, flipType=True)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

    cv2.imshow('Video', frame)


    if(cv2.waitKey(20) & 0xFF==ord('q')):
        break

while not gameOver:
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
          cv2.imshow('Squid Game',cv2.resize(kill, (0,0),fx=0.69,fy=0.69))
    while True:
          cv2.imshow('squid game',cv2.resize(kill,(0,0),fx=0.69,fy=0.69))
          if cv2.waitKey(10) & 0xFF==ord('q'):
               break 
else:
        cv2.imshow('Squid Game', cv2.resize(winner, (0,0), fx=0.69, fy=0.69))
        cv2.waitKey(25)
        
        while True:
            cv2.imshow('Squid Game', cv2.resize(winner, (0,0), fx=0.69, fy=0.69))
            if cv2.waitKey(10) & 0xFF==ord('q'):
                break
            
cam.release()  
cv2.destroyallwindows()     
  #itnaa hii hopayaa 
  # at my limit   







    
   