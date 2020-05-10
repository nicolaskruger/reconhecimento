import cv2
import os
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

    def procTeste(self,img):
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for c in self.cfl:
            faces = c.detectMultiScale(gray)
            for x, y, w, h in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0))
        return img
         

# proc = Proc() 
# img = getImage()
# img = proc.procTeste(img)
# height, width = img.shape[:2]
# img = cv2.resize(img,(int(width/2),int (height/2)), interpolation = cv2.INTER_CUBIC)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()