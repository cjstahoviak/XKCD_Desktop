'''

    Downloads the latest XKCD comic and makes it the desktop background!

'''

import datetime
import urllib.request
import cv2

print("Starting XKCD")

html_file = "index.html"
title_line = None
comic_title = None
comic_image = "comic.png"
back_image = "back_texture.png"
final_image = "final.png"



# Fine the line in the comic with the right name
def GrabImage():
    d = datetime.datetime.today()
    date = '"' + str(d.year) + "-" + str(d.month)  + "-" + str(d.day) + '"'
    html_key = "title=" + date + ">"
    new_comic_found = False
    n = 1

    # The comic's title is listed next to the 
    # current date, find that and parse it out
    while new_comic_found == False: 
        searchfile = open(html_file, "r")
        for line in searchfile:
            if html_key in line: 
                print(line)
                comic_title = line
                new_comic_found = True

        if new_comic_found == True:
            searchfile.close()
            break
        else:
            d = (datetime.datetime.today() - datetime.timedelta(days=n))
            n = n + 1
            date = '"' + str(d.year) + "-" + str(d.month)  + "-" + str(d.day) + '"'
            html_key = "title=" + date + ">"

        
    # Concatenatethe image url using the comics title
    # Thank god he always titles them this way
    if new_comic_found == True:
        print("New Comic Found")
        # Grab title from html line
        comic_title = comic_title.split('>', 1)[-1]
        comic_title = comic_title.split('<', 1)[0].lower()
        comic_title = comic_title.replace(" ", "_")
        comic_title = comic_title.replace("-", "_")
        print("Title: " + comic_title)
        image_url = "https://imgs.xkcd.com/comics/" + comic_title + ".png"

        # Download the image
        urllib.request.urlretrieve(image_url, comic_image)
        return 1

    else:
        return 0

# Let's create the final background and save it to a new image file
def OpenCVWork():
    s_img = cv2.imread(comic_image)
    s_height, s_width, s_channels = s_img.shape
    s_img = cv2.resize(s_img, (2*s_width, 2*s_height), interpolation = cv2.INTER_CUBIC)    # Double the image size
    s_img = cv2.copyMakeBorder(s_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255,255,255))
    s_img = cv2.copyMakeBorder(s_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, (0,0,0))
    s_height, s_width, s_channels = s_img.shape

    l_img = cv2.imread(back_image)
    l_height, l_width, l_channels = l_img.shape

    x_offset = int((l_width - s_width) / 2)
    y_offset = int((l_height - s_height) / 2)
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

    final_image = l_img

    #blur = cv2.GaussianBlur(l_img, (1,1), 0)
    #final_image = cv2.addWeighted(blur, 1.5, l_img, -0.5, 0)

    cv2.imwrite('new_background.png',final_image)

if __name__ == '__main__':
    if GrabImage() == 1:
        OpenCVWork()

