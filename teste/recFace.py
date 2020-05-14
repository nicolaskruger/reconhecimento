import cv2
import os
import time
cv2path = os.path.dirname(cv2.__file__)

def find(name, path):
    for root, dirs, files in os.walk(path):
        if (name in files) or (name in dirs):
            return os.path.join(root, name)
            # Caso nao encontre, recursao para diretorios anteriores
    return find(name, os.path.dirname(path))

xml_path = find('haarcascade_upperbody.xml', cv2path)
print('dir:')
print(xml_path)
clf = cv2.CascadeClassifier(xml_path)
print(clf)

cap = cv2.VideoCapture(0)
while(not cv2.waitKey(20) & 0xFF == ord('q')):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # TODO: Classificar
    t1 = time.time()
    faces = clf.detectMultiScale(gray)
    t1 = time.time()-t1
    print(t1)
        # TODO: Desenhar retangulo
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0))   
    cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

