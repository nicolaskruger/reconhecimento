from pynput.mouse import Button,Controller
import cv2
import os
import time
import threading
lock = threading.Lock()
class Oper(threading.Thread): 
    def __init__(self):
        threading.Thread.__init__(self)
        self.mouse = Controller()
        self.cont = 0
        self.a = True
        self.b = False
    def getLock(self,func):
        lock.acquire()
        A = func()
        lock.release()
        return A
    def get_a(self):
        return self.a
    def getA(self):
        return self.getLock(self.get_a)
    def get_b(self):
        return self.b
    def getB(self):
        return self.getLock(self.get_b)
    
    def setLock(self,func,val):
        lock.acquire()
        func(val)
        lock.release()
    def set_a(self,val):
        self.a=val
    def setA(self,val):
        self.setLock(self.set_a,val)
    def set_b(self,val):
        self.b=val
    def setB(self,val):
        self.setLock(self.set_b,val)
    
    def run(self):
        while self.getA():
            if self.getB():
                self.mouse.click(Button.left,3)
            time.sleep(0.2)

    
    
        
            
    
