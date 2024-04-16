import math as m
import vectors as v
import os
import random as r
import objects as o


"""
for checking intersection:
planes:
parameters needed:
look distance
origin (or position) !
direction !
"""
position=[0,0,0]
direction=[0,1,0]
triangle=[[-1,2,1],[-1,2,-1],[1,2,0]]
distance=12


def volume(a,b,c,d):
    v1=v.minus(b,a)
    v2=v.minus(c,a)
    v3=v.minus(d,a)
    out=v.dot(v.cross(v1,v2),v3)/6
    return out


def intersect(pos,dir,points,distance):
    dir=v.unit(dir)
    q1=pos
    q2=v.add(pos,v.multiply(dir,distance))
    out=0
    bound=range(0,len(points))
    dists=[]
    for i in bound:
        p1=points[i][0]
        p2=points[i][1]
        p3=points[i][2]
        vol1=volume(q1,p1,p2,p3)
        vol2=volume(q2,p1,p2,p3)
        vol3=volume(q1,q2,p1,p2)
        vol4=volume(q1,q2,p2,p3)
        vol5=volume(q1,q2,p3,p1)
        if not v.sameSign2(vol1,vol2):
            if v.sameSign3(vol3,vol4,vol5):
                dist=v.linePlaneDist(pos,dir,distance,points[i])
                dists.append(dist)
    if len(dists)==0:
        return 0
    else:
        return max(dists)



def castRays(dim,pos,dir,points,dist,fovx):
    out=[]
    n=0
    global directions
    directions = []
    wid: int=dim[0]
    height: int=dim[1]
    fovx=fovx*m.pi/180
    alpha=wid/(m.tan(fovx/2))
    dirA=v.multiply(dir,alpha)
    w0=v.unit(v.cross(dir,[0,0,1]))
    h0=v.unit(v.cross(dir,w0))
    topLeftDir=v.minus(v.minus(dirA,v.multiply(h0,(height-1)/2)),v.multiply(w0,(wid-1)/2))
    for h in range(0,height):
        out.append([])
        for w in range(0,wid):
            incw=v.multiply(w0,w)
            inch=v.multiply(h0,h)
            currentDir=v.unit(v.add(v.add(topLeftDir,inch),incw))
            directions.append(currentDir)
            intPoint=intersect(pos,currentDir,points,dist)
            out[h].append(intPoint*255)
    return out






