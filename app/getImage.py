import cv2
import os
import pyscreenshot as ImageGrab
import cv2
import numpy as np
def getImageTeste():
    return cv2.imread("./../data/imageTeste01.jpg")
def getCapturaTela():
    return np.array(ImageGrab.grab().convert('RGB'))
def getImage():
    return getCapturaTela()