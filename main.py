from PIL import Image
im = Image.open("test2.png")
#im.show()

#test img dimensions are 320px by 320px

#box = (100, 100, 200, 200)
#region = im.crop(box)


def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    
    #im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    temp2 = Image.new('RGBA', im.size)
    
    #temp2.paste(part1, (xsize - delta, 0, xsize, ysize))
    temp2.paste(part2, (0, 0, xsize - delta, ysize))
    #temp2.paste()
    return temp2
"""
img = Image.open("test.png").convert('RGB')
print(img)
temp = img.load()
print(img.getdata())
"""

im = Image.open("test7.png").convert('RGBA')
pix_val=list(im.getdata())
"""
pix_val_flat=[]
for group in pix_val:
    for item in group:
        pix_val_flat.append(item)
"""


def getMinBounds(bg, img):
    #bg will be a tuple of rgba, which is the background color
    #img is the image that we're gonna process
    
    img = img.convert('RGBA')
    pixel_map = list(img.getdata())

    def formatHorizontally(width): #groups go from Left to Right
        ret_me = []
        cur_row = set()
        row_count = 0;
        for i in range(len(pixel_map)):
            cur_row.add(pixel_map[i])
            row_count += 1;
            if row_count == width:
                ret_me.append(cur_row)
                cur_row = set()
                row_count = 0;
        return ret_me
    
    def formatVertically(width):
        res = [set() for index in range(width)]
        cur_col = 0;
        for i in range(len(pixel_map)):
            res[cur_col].add(pixel_map[i])
            cur_col += 1;
            if cur_col == width:
                cur_col = 0;
        return res

    hori_ver = formatHorizontally(img.size[0]) #gets width
    
    vert_ver = formatVertically(img.size[0])
    

    def checkNorth():
        for i in pixel_map:
            pass

    return None

#print(pix_val)
getMinBounds((0, 0, 0, 0), im)