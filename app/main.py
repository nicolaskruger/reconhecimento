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
text = ""
def getNum(key):
    if key == ord('u'):
        encr()
    elif key == ord('i'):
        decr()
    elif key == ord('o'):
        pTogle()
    elif key == ord('p'):
        oTogle()
    elif key == ord('j'):
        dimTogle()
    elif key == ord('k'):
        gTogle()
    elif key == ord('n'):
        return 16
    else:
        return curNum


mx = 5
mn = 1
cur = 5
def decr():
    global mx 
    global cur
    global mn
 
    if(cur>mn):
        cur-=1
def encr():
    global mx 
    global cur
    global mn
    
    if(cur<mx):
        cur+=1
def dimTogle():
    procImg.toogleDim()
def gImg0():
    global text
    text+=" "
    text+=procImg.state
    return getImage()
def gImg1():
    global text
    text+=" "
    text+=procImg.state
    img = cv2.imread("./../data/imageTeste05.jpg")
    height, width = img.shape[:2]
    img = cv2.resize(img,(int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)
    return img
gFunc = gImg0
def gTogle():
    global gFunc
    if gFunc == gImg0:
        gFunc =gImg1
    else:
        gFunc = gImg0
def gImage():
    return gFunc()

def pImg00(img):
    global text
    text += " 0"
    return False,img
def pImg01(img):
    global text
    text += " "
    text+=str(cur)
    return procImg.procP(img,cur)
pFunc = pImg01
def pTogle():
    global pFunc
    if pFunc == pImg00:
        pFunc = pImg01
    else:
        pFunc = pImg00
def pImage(img):
    return pFunc(img)

def oImgOper(B):
    global text
    text +=" Oper"
    op.set_b(B)
def oImgNoper(B):
    global text
    text +=" Noper"
    op.set_b(False)
oFunc = oImgNoper
def oTogle():
    global oFunc
    if oFunc == oImgNoper:
        oFunc = oImgOper
    else:
        oFunc = oImgNoper
def oImage(B):
    oFunc(B)
def fImg0(img):
    return format(img)
fFunc = fImg0
def fImage(img):
    return fFunc(img)


def uImg(img):
    u.txt = text
    u.showText(img)
uFunc = uImg
def uImage(img):
    return uFunc(img)

key = cv2.waitKey(1) & 0xFF
while(not key == ord('q')):
    t1 = time.time()
    key = cv2.waitKey(1) & 0xFF
    curNum = getNum(key)
    #switcher.get(curNum)()
    img = gImage()
    B,img = pImage(img)
    oImage(B)
    img = fImage(img)
    uImage(img)
    cv2.imshow("img",img)
    t1 = time.time() - t1
    text = str(round(1/t1,2))
op.setA(False)
op.join()
cv2.destroyAllWindows()
cv2.waitKey(1)