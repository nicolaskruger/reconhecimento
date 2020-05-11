import cv2
import os
import pyscreenshot as ImageGrab
import numpy as np
def getImageTeste():
    return cv2.imread("./../data/imageTeste01.jpg")
def getCapturaTela():
    img= np.array(ImageGrab.grab())
    img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]
    scale = 0.5
    nH = int(h*scale)
    nW = int(w*scale)
    y = int((h-nH)/2)
    x = int((w-nW)/2)
    return img[y:y+nH, x:x+nW]
def getImage():
    return getCapturaTela()