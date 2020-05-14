import time

import cv2
import mss
import numpy
monitor = {"top": 0, "left": 0, "width": 1024, "height": 768}
def getImageTeste():
    return cv2.imread("./../data/imageTeste01.jpg")
def getCapturaTela():
    with mss.mss() as sct:
    #img= np.array(ImageGrab.grab())
    #img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        img = numpy.array(sct.grab(monitor))
        height, width = img.shape[:2]
        img = cv2.resize(img,(int(width/2.7), int(height/2.7)), interpolation = cv2.INTER_CUBIC) 
        return img#[y:y+nH, x:x+nW]
def getImage():
    return getCapturaTela()
