from getImage import getImage
import cv2
from procImage import Proc

procImg = Proc()
while(not cv2.waitKey(20) & 0xFF == ord('q')):
    img = getImage()
    img = procImg.procTeste(img)
    cv2.imshow("img",img)
cv2.destroyAllWindows()
cv2.waitKey(1)