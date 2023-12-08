import cv2
import pandas as pd
import numpy as np

########################################################################################
#   Image Processing Function
########################################################################################

def canny(image):
    return cv2.Canny(image, 100, 200)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def sharpen(image):
    #kernel = np.array([[-0.1,-0.1,-0.1], [-0.1,1.8,-0.1], [-0.1,-0.1,-0.1]])
    #k3=0    # 24
    k2=-0.1
    k1=-5
    k0=-(k2*16+k1*8)+1
    kernel = np.array([
        [k2,k2,k2,k2,k2,], 
        [k2,k1,k1,k1,k2,], 
        [k2,k1,k0,k1,k2,], 
        [k2,k1,k1,k1,k2,], 
        [k2,k2,k2,k2,k2,]
        ])
    
    '''
    k0=-0.02    # 19
    k1=-0.05    # 13
    k2=-2     # 8
    k3=18        # 1
    
    kernel = np.array([
        [k0,k0,k0,k0,k0,k0,k0], 
        [k0,k1,k1,k1,k1,k1,k0], 
        [k0,k1,k2,k2,k2,k1,k0], 
        [k0,k1,k2,k3,k2,k1,k0], 
        [k0,k1,k2,k2,k2,k1,k0], 
        [k0,k1,k1,k1,k1,k1,k0],
        [k0,k0,k0,k0,k0,k0,k0]
        ])'''
    #kernel = np.array([[0.5,0,-0.5], [0.5,0,-0.5], [0.5,0,-0.5]])
    #kernel = (1/(10**2))*np.ones((10,10))
    # https://youtu.be/KuXjwB4LzSA?si=mt-leKGKjpMnJGfg
    # https://www.geeksforgeeks.org/python-opencv-filter2d-function/
    return cv2.filter2D(image, -1, kernel)

#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    # https://www.geeksforgeeks.org/erosion-dilation-images-using-opencv-python/

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#White
def WhiteBackGround(img):
    RangeMax=100
    A1=1
    Step=1
    Start=0
    for i in range(RangeMax):
      mark=np.logical_and(img>Start+(i*Step)/A1,img<Start+((i+1)*Step)/A1)
      img[mark]=Start+(i*Step)/A1
    img[img>=Start+((RangeMax)*Step)/A1]=255
    return img

########################################################################################
#   Display the Image
########################################################################################

def ShowMustGoOn(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
path='/Users/imac/Desktop/SoloOpenSourceProject/JOCR/TestImage/Expenses_Macro/IMG_7553.jpeg'
img = cv2.imread(path)
img = get_grayscale(img)
#print(type(img))
#print(img.shape)
#img = erode(img)
img = sharpen(img)
#img = dilate(img)
ShowMustGoOn(img)
'''

'''
python3 kernel.py
'''