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

im = Image.open("test14.png").convert('RGBA')
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
    width , height = img.size #img.size returns (width, height) as a tuple

    def formatHorizontally(): #groups go from Left to Right
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
    
    def formatVertically():
        res = [set() for index in range(width)]
        cur_col = 0;
        for i in range(len(pixel_map)):
            res[cur_col].add(pixel_map[i])
            cur_col += 1;
            if cur_col == width:
                cur_col = 0;
        return res
    
    def checkNorth(): #it's inclusive
        north_bound = 0;
        for row in hori_ver:
            if (bg in row and len(row) > 1) or (bg not in row):
                break
            else:
                north_bound += 1;
        return north_bound
    
    def checkSouth(): #it's inclusive
        south_bound = height
        temp_hori = hori_ver
        temp_hori.reverse();
        for row in temp_hori:
            if (bg in row and len(row) > 1) or (bg not in row):
                break
            else:
                south_bound -= 1;
        return south_bound
    
    def checkWest():
        west_bound = 0;
        for row in vert_ver:
            if (bg in row and len(row) > 1) or (bg not in row):
                break
            else:
                west_bound += 1;
        return west_bound

    def checkEast(): #it's inclusive
        east_bound = width
        temp_vert = vert_ver
        temp_vert.reverse();
        for row in vert_ver:
            if (bg in row and len(row) > 1) or (bg not in row):
                break
            else:
                east_bound -= 1;
        return east_bound

    hori_ver = formatHorizontally()
    vert_ver = formatVertically()
    """
    print("North Boundary: " , checkNorth())
    print("South Boundary: " , checkSouth())
    print("West Boundary: " , checkWest())
    print("East Boundary: " , checkEast())
    """
    minBounds = (checkWest(), checkNorth(), checkEast(), checkSouth())
    return minBounds

#print(pix_val)
getMinBounds((255, 255, 255, 255), im) #returns a tuple of where you crop




xsize, ysize = im.size
box = (2, 3, 6, 9) #the proper crop for test8.png

box = getMinBounds((255, 255, 255, 255), im) #returns a tuple of where you crop


temp2 = Image.new('RGBA', im.size)
cropped = im.crop(box)

temp2.paste(cropped, box)

temp2.show()
"""
part1 = im.crop((0, 0, delta, ysize))
part2 = im.crop((delta, 0, xsize, ysize))


temp2 = Image.new('RGBA', im.size)

temp2.paste(part1, (xsize - delta, 0, xsize, ysize))
temp2.paste(part2, (0, 0, xsize - delta, ysize))"""