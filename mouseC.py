from pynput.mouse import Button,Controller
import cv2
import os
import time
from pynput.keyboard import Listener
# K='a'
# def wK(key):
#     K=key
#     print(K)
# def contMouse():
#     mouse = Controller()
#     while(K!='q'):
#         mouse.release(Button.left)
#         time.sleep(1)
#         print(mouse.position)
# with Listener(on_press=wK) as L:
#     L.join()
img = cv2.imread("p2.png")
cv2.imshow("Video", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# while (True):
#     k = cv2.waitKey(500) & 0xFF
#     # press 'q' to exit
#     print(k)
#     if k == ord('q'):
#         break

        # change a variable / do something ...

