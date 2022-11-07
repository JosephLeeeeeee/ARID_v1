import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from skimage import io
img = io.imread('data/img_00001.jpg')
type(img)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()