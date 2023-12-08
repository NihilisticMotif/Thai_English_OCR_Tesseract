import pytesseract as ts
from PIL import Image
import cv2
import pandas as pd
import numpy as np
from kernel import canny,get_grayscale,sharpen,erode,dilate,opening,ShowMustGoOn,WhiteBackGround
import os

# https://stackoverflow.com/questions/54725151/pytesseract-tesseracterror-usage-python-pytesseract-py-l-lang-input-file

path = "/mnt/c/Users/Admin/Documents/GitHub/Thai_English_OCR_Tesseract/DataSet/IMG_7553.jpeg"

img = cv2.imread(path)
img = get_grayscale(img)
img = sharpen(img)
img = WhiteBackGround(img)
img=img[1100:,:]#600:2000]   

# To convert from OpenCV image to PIL image use:
# https://stackoverflow.com/questions/43232813/convert-opencv-image-format-to-pil-image-format
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = Image.fromarray(img)
cv2.imshow('window_name', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

# Convert Image to text using OCR
# https://stackoverflow.com/questions/64723694/permission-denied-when-reading-a-image-text-in-pytesseract
#img=Image.open(img)

txt=ts.image_to_string(img, 
                       lang='eng', 
                       config='--psm 6',
                       #config="--psm 13"
                       )
# lang='tha'
# lang='eng'
# lang='eng+tha'

print(txt)

#txt=''.join(str(txt).split(' '))
#eraser('demo.txt')
#pensil('demo.txt',txt)

'''
python print.py
'''
