from os import listdir
from os.path import isfile, join
from PIL import Image
from img_utils import getMinBounds #WNES

dir = "input"
filePaths = [f for f in listdir(dir) if isfile(join(dir, f))]

index = 0
background_color = (0, 0, 0, 0);
max_h = None;
max_w = None;
for path in filePaths:
    im = Image.open(dir + "/" + path).convert('RGBA')
    pix_val = list(im.getdata())
    box = getMinBounds(background_color, im) #returns a tuple of where you're cropping
    #print(box)
    
    width = box[2] - box[0]
    height = box[3] - box[1]
    if max_h == None:
        max_h = height;
    else:
        max_h = max(height, max_h)
    if max_w == None:
        max_w = width;
    else:
        max_w = max(width, max_w)
    
    #print(box)
    
    #print("Width: " , width , ", Height: " , height)
    #print()

    """
    cropped = im.crop(box)
    new_name = "tile0"
    if index < 10:
        new_name += "0"
    new_name += str(index) + ".png"
        
    cropped.save("output/" + new_name)
    index += 1;
    """
print()

for path in filePaths:
    im = Image.open(dir + "/" + path).convert('RGBA')
    pix_val = list(im.getdata())
    box = getMinBounds(background_color, im) #returns a tuple of where you're cropping
    start = (box[2], box[3])
    #print(dir + "/" + path )
    fixed_box = (start[0] - max_w, start[1] - max_h, start[0], start[1])
    cropped = im.crop(fixed_box)
    new_name = "tile0"
    if index < 10:
        new_name += "0"
    new_name += str(index) + ".png"
        
    cropped.save("output/" + new_name)
    index += 1;

print("Maxes: " , max_w , ", " , max_h)

"""
getMinBounds() output:
West, north, east, south
(x1, y1, x2, y2)

top left corner coords and bottom right corner coord
(x1, y1)
(x2, y2)

"""