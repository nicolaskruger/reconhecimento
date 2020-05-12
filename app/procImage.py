import cv2
import os
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
        self.dim = {
            "haarcascade_frontalface_alt2.xml": [-1/2,-1/5,2,8,0],
            "haarcascade_fullbody.xml": [0,0,1,1,0],
            "haarcascade_lowerbody.xml": [0,-2.3,1,3.1,0],
            "haarcascade_upperbody.xml": [0,0,1,3,0],
            "haarcascade_profileface.xml": [-1/2,-1/5,2,8,0],
        }
        self.total = 0
        self.getCascadeClassifier()

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
    def procTeste(self,img):
        h, w = img.shape[:2]
        centerX = int(w/2)
        centerY = int(h/2)
        B = False
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trh = []
        for i in range(len(self.cfl)):
            pos = self.dim[self.lOfLinks[i]]
            tr =prThread(gray[:],self.cfl[i],pos[0],pos[1],pos[2],pos[3])
            tr.start()
            trh.append(tr)
        for tr in trh:
            tr.join()
        
        for tr in trh:
           tr.drawAll(img)
        self.calcPercente(trh)
        return B,img
         

# proc = Proc() 
# img = getImage()
# img = proc.procTeste(img)
# height, width = img.shape[:2]
# img = cv2.resize(img,(int(width/2),int (height/2)), interpolation = cv2.INTER_CUBIC)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()