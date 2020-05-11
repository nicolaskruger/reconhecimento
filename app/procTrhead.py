import cv2
import threading



class prThread (threading.Thread): 
    def __init__(self, img, cfl):
        threading.Thread.__init__(self)
        self.img = img
        self.cfl = cfl
        self.face = 0
    def run(self):
        self.face = self.cfl.detectMultiScale(self.img)
    def getFaces():
        return self.face