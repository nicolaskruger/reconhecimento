import pyscreenshot as ImageGrab
import cv2
import numpy as np
imagem = np.array(ImageGrab.grab().convert('RGB'))
cv2.imshow("img",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
#imagem.save('screenShot1.jpg', 'jpeg')
