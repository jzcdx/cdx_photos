from PIL import Image

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

#box = (2, 3, 6, 9) #the proper crop for test8.png
"""
im = Image.open("test_images/test14.png").convert('RGBA')
pix_val=list(im.getdata())
box = getMinBounds((0, 0, 0, 255), im) #returns a tuple of where you crop

temp2 = Image.new('RGBA', im.size)
cropped = im.crop(box)
cropped.save("output/temp.png")
"""
