import cv2
import os
import pyscreenshot as ImageGrab
import numpy as np
def getImageTeste():
    return cv2.imread("./../data/imageTeste01.jpg")
def getCapturaTela():
    img= np.array(ImageGrab.grab())
    img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.equalizeHist(img)
    #h, w = img.shape[:2]
    #scale = 0.5
    # nH = int(h*scale)
    # nW = int(w*scale)
    #size = 100
    #x = int(w/2)-int(size/2)
    #y = int(h/2)-int(size/2)
    
    #cv2.rectangle(img, (x,y) ,(x+ size,y+ size), (0, 255, 0))
    return img#[y:y+nH, x:x+nW]
def getImage():
    return getCapturaTela()
