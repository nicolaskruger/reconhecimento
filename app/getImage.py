import cv2

def getImageTeste():
    return cv2.imread("./../data/imageTeste.jpg")
def getImage():
    return getImageTeste()
img =getImage()
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()