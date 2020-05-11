from pynput.mouse import Button,Controller
import cv2
import os
import time

class Oper: 
    def __init__(self):
        self.mouse = Controller()
    def oper(Bool):
        if Bool:
            self.mouse.click(Button.left,1)
