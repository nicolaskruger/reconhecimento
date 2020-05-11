import cv2
import os
import threading
from procTrhead import prThread
from getImage import getImage
cv2path = os.path.dirname(cv2.__file__)
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
        print(self.lOfLinks)
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
        print([x0,y0,x,y,w,h])
        return (x< x0<(x+w)) and (y < y0<(y+h))

    def procTeste(self,img):
        h, w = img.shape[:2]
        centerX = int(w/2)
        centerY = int(h/2)
        B = False
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trh = []
        for c in self.cfl:
            tr =prThread(gray[:],c)
            tr.start()
            trh.append(tr)
        for tr in trh:
            tr.join()
        
        for tr in trh:
           for x, y, w, h in tr.face:
                print([x,y,w,h])
                if(self.coliding(centerY,centerX,x,y,w,h)):
                    B=True
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255))
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0))
        return B,img
         

# proc = Proc() 
# img = getImage()
# img = proc.procTeste(img)
# height, width = img.shape[:2]
# img = cv2.resize(img,(int(width/2),int (height/2)), interpolation = cv2.INTER_CUBIC)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()