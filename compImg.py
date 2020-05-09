from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('p1.png')) 
hash1 = imagehash.average_hash(Image.open('p2.png')) 
cutoff = 5

if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')