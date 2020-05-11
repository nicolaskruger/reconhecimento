from getImage import getImage
import cv2
from procImage import Proc
from oper import Oper
import time
from userInterface import UI
from fromatImag import format

procImg = Proc()
op = Oper()
u =UI(2)
curNum=1
def getNum(key):
    if key == ord('u'):
        return 10
    elif key == ord('i'):
        return 11
    elif key == ord('o'):
        return 12
    else:
        return curNum
def tipe0():
    img = getImage()
    img = format(img)
    cv2.imshow("img",img)
def tipe1():
    img = getImage()
    B,img = procImg.procTeste(img)
    img = format(img)
    img = u.showAll(img)
    cv2.imshow("img",img)
def tipe2():
    img = getImage()
    B,img = procImg.procTeste(img)
    img = format(img)
    img = u.showAll(img)
    cv2.imshow("img",img)
def set0():
    print("tipe0")
    global curNum
    curNum = 0
def set1():
    print("tipe1")
    global curNum
    curNum = 1
    u.changeColor(0,u.red())
def set2():
    print("tipe2")
    global curNum
    curNum = 2
    u.changeColor(0,u.green())
switcher = {
        0: tipe0,
        1: tipe1,
        2: tipe2,
        10: set0,
        11: set1,
        12: set2,
    }
key = cv2.waitKey(1) & 0xFF
while(not key == ord('q')):
    key = cv2.waitKey(1) & 0xFF
    curNum = getNum(key)
    switcher.get(curNum)()
cv2.destroyAllWindows()
cv2.waitKey(1)