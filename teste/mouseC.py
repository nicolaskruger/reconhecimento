from pynput.mouse import Button,Controller
import cv2
import os
import time

mouse = Controller()
po = (0,0)
mouse.click(Button.right,1)
while mouse.position!=po:
    mouse.release(Button.left)
    
        # change a variable / do something ...

