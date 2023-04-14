from os import listdir
from os.path import isfile, join
from PIL import Image
from img_utils import getMinBounds

dir = "input"
filePaths = [f for f in listdir(dir) if isfile(join(dir, f))]

"""
im = Image.open("test_images/test14.png").convert('RGBA')
pix_val=list(im.getdata())
box = getMinBounds((0, 0, 0, 255), im) #returns a tuple of where you crop

temp2 = Image.new('RGBA', im.size)
cropped = im.crop(box)
cropped.save("output/temp.png")
"""

index = 0
for path in filePaths:

    im = Image.open(dir + "/" + path).convert('RGBA')
    pix_val=list(im.getdata())
    box = getMinBounds((0, 0, 0, 0), im) #returns a tuple of where you crop

    temp2 = Image.new('RGBA', im.size)
    cropped = im.crop(box)
    new_name = "tile0"
    if index < 10:
        new_name += "0"
    new_name += str(index) + ".png"
        
    cropped.save("output/" + new_name)
    index += 1;


im = Image.open("test_images/test14.png").convert('RGBA')
pix_val=list(im.getdata())
box = getMinBounds((0, 0, 0, 255), im) #returns a tuple of where you crop

temp2 = Image.new('RGBA', im.size)
cropped = im.crop(box)
cropped.save("output/temp.png")
