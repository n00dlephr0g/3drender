import math as m
from PIL import Image as image
import numpy as np


def getImageBW(filename):
    #converts image to matrix of gamma value from 0 to 255
    #input: filename
    #   relative path of image as a string
    try:
        type(filename) == str
    except:
        print("getImage file name is not string")
    out=[]
    pic=image.open(filename)
    width,height=pic.size
    for h in range(0,height):
        out.append([])
        for w in range(0,width):
            rgb=pic.getpixel((w,h))
            gamma=getGamma(rgb[0],rgb[1],rgb[2])
            out[h].append(gamma)
    return out

def convertTo92(img):
    out=[]
    for h in range(0,len(img)):
        out.append([])
        for w in range(0,len(img[h])):
            char = round(img[h][w]/2.7826)
            out[h].append(char)
    return out


def getGamma(R,G,B):
    Y = 0.2126*R + 0.7152*G + 0.0722*B
    return Y

