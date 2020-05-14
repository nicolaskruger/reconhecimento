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
        self.cont=0
    def run(self):
        self.face = self.cfl.detectMultiScale(self.img)
    def getFaces(self):
        return self.face
    def coliding(self,x0,y0,x,y,w,h,img):
        side = 100
        x0 -= int(side/2)
        y0 -= int(side/2)
        w0 = x0+side
        h0 = y0+side
        cv2.rectangle(img, (x0, y0), (w0, h0), (0, 255, 0))
        w+=x
        h+=y

        X0 = [x0,w0,x,w]
        X1 = [x,w,x0,w0]
        Xo = sorted(X0)
        if(Xo==X0 or Xo==X1):
            return False
        
        Y0 = [y0,h0,y,h]
        Y1 = [y,h,y0,h0]
        Yo = sorted(Y0)
        if(Yo==Y0 or Yo==Y1):
            return False
        return True
    def checkAll(self,img):
        h, w = img.shape[:2]
        centerX = int(w/2)
        centerY = int(h/2)
        for x, y, w, h in self.face:
                self.cont+=1
                x,y,w,h= self.resize(x,y,w,h)
                if(self.coliding(centerX,centerY,x,y,w,h,img)):
                    return True
        return False
    def drawAll(self,img):
        h, w = img.shape[:2]
        centerX = int(w/2)
        centerY = int(h/2)
        B=False
        for x, y, w, h in self.face:
                self.cont+=1
                x,y,w,h= self.resize(x,y,w,h)
                if(self.coliding(centerX,centerY,x,y,w,h,img)):
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
        