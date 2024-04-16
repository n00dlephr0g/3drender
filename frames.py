import os
import math as m
import time as t
import random as r
import handlingImage as hi


ascii=[
    ' ','`', '.', '-', "'", ':', '_', ',', '^', '=', ';', '>', '<', '+', '!', 'r', 'c', '*', '/', 'z', '?', 's', 'L', 'T', 'v', ')', 'J', '7', '(', '|', 'F', 'i', '{', 'C', '}', 'f', 'I', '3', '1', 't', 'l', 'u', '[', 'n', 'e', 'o', 'Z', '5', 'Y', 'x', 'j', 'y', 'a', ']', '2', 'E', 'S', 'w', 'q', 'k', 'P', '6', 'h',  '9', 'd', '4', 'V', 'p', 'O', 'G', 'b', 'U', 'A', 'K', 'X', 'H', 'm', '8', 'R', 'D', '#', '$', 'B', 'g', '0', 'M', 'N', 'W', 'Q', '%', '&', '@'
    ] #92 characters

#standard fram format is brightness matrix

def genBlankFrame(dim):
    out=[]
    width=dim[0]
    height=dim[1]
    for h in range(0,height):
        out.append([])
        for w in range(0,width):
            out[h].append(' ')
    return out

def genNumFrame(dim,lower,upper):
    try:
        int(lower)
        int(upper)
    except:
        print("genRandFrame bounds not integers")
    out=[]
    width=dim[0]
    height=dim[1]
    for h in range(0,height):
        out.append(list())
        for w in range(0,width):
            out[h].append(r.randint(lower,upper))
    return out


def genListFrame(dim,list):
    out=[]
    width=dim[0]
    height=dim[1]
    upper=len(list)-1
    for h in range(0,height):
        out.append([])
        for w in range(0,width):
            out[h].append(list[r.randint(0,upper)])
    return out


def genAsciiFrame(frameout):
    out=[]
    wid=len(frameout[0])
    for h in range(0,len(frameout)):
        out.append([])
        for w in range(0,wid):
            pixelVal=round((frameout[h][w]/2.81318))
            out[h].append(ascii[pixelVal])
    return out


def genLine(line,scale):
    out=""
    for i in line:
        for s in range(0,scale):
            out=out+f"{i}"*2+' '
    return out

def printFrame(frameout):
    wid=len(frameout[0])
    line=None
    for h in range(0,len(frameout)):
        for w in range(0,wid):
            line=genLine(frameout[h],1)
        print(line)

def printFrameScale(frameout,scale):
    line=None
    for h in range(0,len(frameout)):
        for w in range(0,len(frameout[h])):
            line=genLine(frameout[h],scale)
        for i in range(0,scale):
            print(line)


def overlay(frame,element,pos):
    out=frame
    w0=pos[0]
    h0=pos[1]
    fh=len(out)
    fw=len(out[0])
    eh=len(element)
    ew=len(element[0])
    #check if its out of bounds:
    if w0+ew>fw or h0+eh>fh:
        raise Exception('overlay out of bounds')
    for h in range(0,eh):
        for w in range(0,ew):
            out[h0+h][w0+w]=element[h][w]
    return out


def overlayT(frame,element,pos,tolerance):
    out=frame
    w0=pos[0]
    h0=pos[1]
    fh=len(out)
    fw=len(out[0])
    eh=len(element)
    ew=len(element[0])
    #check if its out of bounds:
    if w0+ew>fw or h0+eh>fh:
        raise Exception('overlay out of bounds')
    if 0< tolerance < 255:
        raise Exception('overlayT tolerance out of bounds') 
    for h in range(0,eh):
        for w in range(0,ew):
            pixel=element[h][w]
            if pixel>=tolerance:
                out[h0+h][w0+w]=pixel
    return out


def inverse(frame):
    out=[]
    width=len(frame[0])
    height=len(frame)
    for h in range(0,height):
        out.append([])
        for w in range(0,width):
            out[h].append(255-frame[h][w])
    return out