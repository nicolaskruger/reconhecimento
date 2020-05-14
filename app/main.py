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
curNum=10
op.start()
def getNum(key):
    if key == ord('u'):
        return 10
    elif key == ord('i'):
        return 11
    elif key == ord('o'):
        return 12
    elif key == ord('p'):
        return 13
    elif key == ord('j'):
        return 14
    elif key == ord('k'):
        return 15
    elif key == ord('n'):
        return 16
    else:
        return curNum
def tipe0():
    
    img = getImage()
    img = format(img)
    cv2.imshow("img",img)
def tipe1():
    img = getImage()
    B,img = procImg.procP(img,1)
    op.setB(B)
    img = format(img)
    img = u.showAll(img)
    cv2.imshow("img",img)
def tipe2():
    img = getImage()
    B,img = procImg.procTeste(img)
    img = format(img)
    img = u.showAll(img)
    cv2.imshow("img",img)
def tipe3():
    img = getImage()
    B,img = procImg.procP(img,5)
    op.setB(B)
    img = format(img)
    img = u.showAll(img)
    cv2.imshow("img",img)
def tipe4():
    img = getImage()
    B,img = procImg.procNotRender(img,5)
    op.setB(B)
    #img = format(img)
    #img = u.showAll(img)
    cv2.imshow("img",img)
def tipe5():
    img = getImage()
    B,img = procImg.procNotRender(img,1)
    op.setB(B)
    #img = format(img)
    #img = u.showAll(img)
    cv2.imshow("img",img)
def tipe6():
    img = getImage()
    B,img = procImg.procP(img,3)
    img= format(img)
    cv2.imshow("img",img)
def set0():
    print("tipe0\nsomente a camera")
    global curNum
    curNum = 0
    op.setB(False)
def set1():
    print("tipe1\ncaptura 3 melhores, renderiza e opera")
    global curNum
    curNum = 1
    u.changeColor(0,u.red())
    op.setB(False)
def set2():
    print("tipe2\ncaptura todos melhores , renderiza")
    global curNum
    curNum = 2
    u.changeColor(0,u.green())
    op.setB(False)
def set3():
    print("tipe3\ncaptura todos melhores , renderiza e opera")
    global curNum
    curNum = 3
    u.changeColor(0,u.green())
    op.setB(False)
def set4():
    print("tipe4\ncaptura todos e opera")
    global curNum
    curNum = 4
    u.changeColor(0,u.green())
    op.setB(False)
def set5():
    print("tipe5\ncaptura 1 melhores todos e opera")
    global curNum
    curNum = 5
    u.changeColor(0,u.green())
    op.setB(False)
def set6():
    print("tipe6\nreconhecimento de caracteres, render")
    global curNum
    curNum = 6
    u.changeColor(0,u.green())
    op.setB(False)
switcher = {
        0: tipe0,
        1: tipe1,
        2: tipe2,
        3: tipe3,
        4: tipe4,
        5: tipe5,
        6: tipe6,
        10: set0,
        11: set1,
        12: set2,
        13: set3,
        14: set4,
        15: set5,
        16: set6,
    }
key = cv2.waitKey(1) & 0xFF
while(not key == ord('q')):
    t1 = time.time()
    key = cv2.waitKey(1) & 0xFF
    curNum = getNum(key)
    switcher.get(curNum)()
    t1 = time.time() - t1
    print(chr(27) + "[2J")
    print(1/t1)
op.setA(False)
op.join()
cv2.destroyAllWindows()
cv2.waitKey(1)