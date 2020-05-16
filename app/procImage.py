import cv2
import os
import time
import threading
from procTrhead import prThread
from getImage import getImage
cv2path = os.path.dirname(cv2.__file__)
# haarcascade_frontalface_alt2.xml
# haarcascade_fullbody.xml
# haarcascade_lowerbody.xml
# haarcascade_upperbody.xml
# haarcascade_profileface.xml
def find(name, path):
    for root, dirs, files in os.walk(path):
        if (name in files) or (name in dirs):
            return os.path.join(root, name)
            # Caso nao encontre, recursao para diretorios anteriores
    return find(name, os.path.dirname(path))
class Proc:   
    lOfLinks = []
    cfl = []

    def __init__(self):
        self.func_names()
        #print(self.lOfLinks)
        self.pFundo = cv2.imread("./../data/p11.png")
        
        self.deafDim = {
            "haarcascade_frontalface_alt2.xml": [0,0,1,1,0],
            "haarcascade_fullbody.xml": [0,0,1,1,0],
            "haarcascade_lowerbody.xml": [0,0,1,1,0],
            "haarcascade_upperbody.xml": [0,0,1,1,0],
            "haarcascade_profileface.xml": [0,0,1,1,0],
            "haarcascade_russian_plate_number.xml": [0,0,1,1],
        }
        self.reDim = {
            "haarcascade_frontalface_alt2.xml": [-1,-1/5,3,8,0],
            "haarcascade_fullbody.xml": [0,0,1,1,0],
            "haarcascade_lowerbody.xml": [0,-2.3,1,3.1,0],
            "haarcascade_upperbody.xml": [0,0,1,3,0],
            "haarcascade_profileface.xml": [-1,-1/5,3,8,0],
            "haarcascade_russian_plate_number.xml": [0,0,1,1],
        }
        self.dim = self.reDim
        self.state = "redim"
        self.total = 0
        self.getCascadeClassifier()
    def setDeafDim(self):
        self.state ="deafdim"
        self.dim = self.deafDim
    def setReDim(self):
        self.state ="redim"
        self.dim = self.reDim
    def toogleDim(self):
        if self.dim == self.deafDim:
            self.setReDim()
        else:
            self.setDeafDim()
    def func_names(self):
        f = open("./../data/allxmlNames.txt","r")
        txt = f.readline()
        
        while(txt != ''):
            txt=txt[:-1]
            self.lOfLinks.append(txt)
            txt = f.readline()
        f.close()

    def getCascadeClassifier(self):
        for l in self.lOfLinks:
            xml = find(l,cv2path)
            self.cfl.append(cv2.CascadeClassifier(xml))
    def coliding(self,x0,y0,x,y,w,h):
        return (x< x0<(x+w)) and (y < y0<(y+h))

    def calcPercente(self,trh):
        for i in range(len(trh)):
            self.total += trh[i].cont
            self.dim[self.lOfLinks[i]][4]+=trh[i].cont
        st = ""
        for i in range(len(trh)):
            st+=self.lOfLinks[i]
            st+="= "
            if self.dim[self.lOfLinks[i]][4] != 0:
                st+=str(self.dim[self.lOfLinks[i]][4]/self.total)
        print(st)
    def proc(self,img,func,n,m=0):
        n=n%(len(self.lOfLinks)+1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trh = []
        for i in range(m,n):
            pos = self.dim[self.lOfLinks[i]]
            tr =prThread(gray[:],self.cfl[i],pos[0],pos[1],pos[2],pos[3])
            tr.start()
            trh.append(tr)
        for tr in trh:
            tr.join()
        return func(trh,img)
    def proc_teste(self,trh,img):
        B = False
        for tr in trh:
           if tr.drawAll(img):
               B=True
        self.calcPercente(trh)
        return B,img
    def procTeste(self,img):
        return self.proc(img,self.proc_teste,5)
    def proc_p(self,trh,img):
        B=False
        for tr in trh:
            if tr.drawAll(img):
               B=True
        return B,img
    def procP(self,img,n,m=0):
        return self.proc(img,self.proc_p,n,m)
    def proc_not_render(self,trh,img):
        for tr in trh:
            if tr.checkAll(img):
                return True,self.pFundo
        return False,self.pFundo
    def procNotRender(self,img,n):
        return self.proc(img,self.proc_not_render,n)
# proc = Proc() 
# img = getImage()
# img = proc.procTeste(img)
# height, width = img.shape[:2]
# img = cv2.resize(img,(int(width/2),int (height/2)), interpolation = cv2.INTER_CUBIC)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()