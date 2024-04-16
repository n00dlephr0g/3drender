import math as m
import vectors as v
import frames as f

def compass(angle,size):
    '''
    inputs:
    angle
    size (integer (odd for best result), will be square element)
    '''
    #0 degrees is north
    #90 degrees is east
    element=[]
    lerpn=int((size+1)/2)
    step=1/lerpn
    dir=v.rotate90(v.getDirxy(angle))
    p1=[(size-1)/2,(size-1)/2]
    p2=v.add(v.multiply(dir,-size/2),p1)
    pixels=[p1]
    #getting interpolated points and rounding points, then append to pixels
    for n in range(1,lerpn):
        t=step*n
        pixel=v.lerpVec(p1,p2,t)
        pixels.append(v.roundVec(pixel,0))
    #generates element as brightness matrix
    for h in range(0,size):
        element.append([])
        for w in range(0,size):
            if [w,h] in pixels:
                element[h].append(255)
            else:
                element[h].append(0)
    return element


def gauge(dim,l,u,val):
    element=[]
    wid=dim[0]
    height=dim[1]
    ratio=1-((val-l)/(u-l))
    hvalue=round(ratio*(height-1))
    for h in range(0,height):
        element.append([])
        if h==hvalue:
            for w in range(0,wid):
                element[h].append(255)
        else:
            for w in range(0,wid):
                element[h].append(0)
    return element       



def outline(dim,thickness):
    element=[]
    wid=dim[0]
    height=dim[1]
    a=thickness-1
    b=thickness+1
    for h in range(0,height):
        element.append([])
        if h<=a or h>height-b:
            for w in range(0,wid): #row tahts outline
                element[h].append(255)
        else: #rows that arent
            for w in range(0,wid): 
                if w<=a or w>height-b:
                    element[h].append(255)
                else:
                    element[h].append(0)
    return element   


def map(dim,location,tl,br,scale):
    '''
    inputs:
    centre (top left of map)
    scale (pixels per unit in both directions)'''
    element=[]
    ewid=dim[0]
    eheight=dim[1]
    centre = [(br[0]-tl[0])/2,(br[1]-tl[1])/2]
    for h in range(0,eheight):
        element.append([])
        for w in range(0,ewid):
            pass


