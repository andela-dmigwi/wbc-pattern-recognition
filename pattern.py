from PIL import Image
from pprint import pprint
import numpy

numpy.set_printoptions(threshold=numpy.nan)

try:
    im = Image.open("images/shades_of_purple.png")
except Exception:
    print ("Image not found")
    exit()
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
# Get the RGBA Value of the a pixel of an image
pixel_data = list(im.getdata())
pprint(numpy.asarray(im))
# pprint(pix.shape)
# pprint(pix.size)

# pix[x, y] = value  # Set the RGBA Value of the image (tuple)
# im.show()
