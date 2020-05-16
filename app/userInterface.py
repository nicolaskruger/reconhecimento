from ui import ui
import cv2

class UI:
    def __init__(self, number):
        self.l = []
        for i in range(number):
            self.l.append(ui(5+10*i,5,5,5,self.red()))
        self.txt = "oi"
    def green(self):
        return (0,255,0)
    def red(self):
        return (0,0,255)
    def showAll(self,img):
        for u in self.l:
            img = u.makeRectangle(img)
        return img
    def showText(self,img):
        cv2.putText(img,self.txt, (10,25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0))
    def changeColor(self,num,color):
        self.l[num].setColor(color)