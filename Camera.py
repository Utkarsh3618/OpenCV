# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:50:32 2019

@author: Utkarsh1409
"""

import cv2

def main():
    WindowName="Live Webcam Video Feed Capture"
    cv2.namedWindow(WindowName)
    cap = cv2.VideoCapture(0)
    
    filename=r"C:\Users\Utkarsh1409\Desktop\OpenCV\Output.avi"
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=16
    resolution=(640,480)
    
    VideoFileOutput=cv2.VideoWriter(filename,codec,framerate,resolution)
    
    if cap.isOpened():
        ret, frame =cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame =cap.read()
        VideoFileOutput.write(frame)
        
        cv2.imshow(WindowName,frame)
        if cv2.waitKey(1) ==27:
            break
        
    cv2.destroyWindow(WindowName)
    VideoFileOutput.release()
        
    cap.release()
        
if __name__=="__main__":
    main()