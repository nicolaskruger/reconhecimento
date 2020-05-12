import cv2
import threading



class prThread (threading.Thread): 
    def __init__(self, img, cfl, X,Y,W,H):
        threading.Thread.__init__(self)
        self.img = img
        self.cfl = cfl
        self.face = 0
        self.X=X
        self.Y=Y
        self.W=W
        self.H=H
        self.cont = 0
    
    def run(self):
        self.face = self.cfl.detectMultiScale(self.img)
    def getFaces(self):
        return self.face
    def coliding(self,x0,y0,x,y,w,h):
        return (x< x0<(x+w)) and (y < y0<(y+h))
    def drawAll(self,img):
        h, w = img.shape[:2]
        centerX = int(w/2)
        centerY = int(h/2)
        B=False
        for x, y, w, h in self.face:
                self.cont+=1
                x,y,w,h= self.resize(x,y,w,h)
                if(self.coliding(centerY,centerX,x,y,w,h)):
                    B=True
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255))
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0))
        return B
    def resize(self,x,y,w,h):
        x= int(x+w*self.X)
        w= int(self.W*w)
        y= int(y+self.Y*h)
        h= int(self.H*h)
        return x,y,w,h
        