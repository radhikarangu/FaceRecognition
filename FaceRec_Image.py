# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:28:53 2020

@author: RADHIKA
"""

import cv2
import numpy as np


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread('obama.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)     
    cv2.imshow('img', img)    
    cv2.waitKey() 
    