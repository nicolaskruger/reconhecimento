import cv2


class ui:
    def __init__(self,x,y,w,h,color):
        self.start = (x,y)
        self.end = (x+w,y+h)
        self.color = color
    def makeRectangle(self, img, color):
        return cv2.rectangle(img,self.start,self.end,color,cv2.FILLED)
    def makeRectangle(self, img):
        return cv2.rectangle(img,self.start,self.end,self.color,cv2.FILLED)
    def setColor(self,color):
        self.color = color
    
    