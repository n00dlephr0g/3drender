import math as m
import time as t
import frames as f
import elements as e
import player as p
import vectors as v
import camera as c
import objects as o
import level as l
import os

init=True
#define initial position
pos0 = [0,-4,0]
#define initial direction
angDir0 = [0,0]
direction= [0,1,0]
sphere=o.vertices(o.sphere,[0,m.pi],[0,2*m.pi],2)
distance=12

#o.desmosPoints(sphere)
points=o.genMesh(sphere)


#for i in range(0,len(points)):
    #o.desmosPoints(points[i])


frame=c.castrays([32,32],pos0,direction,points,distance,90)
frame=f.genAsciiFrame(frame)
f.printFrame(frame)

'''
while True:
    try:
        p.controlPlayer(pos0, angDir0, 10,3,0.001,init)
        init=False
        frame=c.castrays([20,15],p.pos,p.direction,points,distance,90)
        os.system('cls')
        print("position: ",v.roundVec(p.pos,2),"\ndirection: ", v.roundVec(p.direction,2))
        print('\n')
        frame=f.genAsciiFrame(frame)
        f.printFrame(frame)
        """ rectile=f.genBlankFrame([13,11])
        compass=f.genAsciiFrame(e.compass(p.angDir,9))
        gauge=f.genAsciiFrame(e.gauge([1,9],-1,1,p.direction[2]))
        outline=f.genAsciiFrame(e.outline([13,11],1))
        rectile=f.overlay(rectile,outline,[0,0])
        rectile=f.overlay(rectile,compass,[2,1])
        rectile=f.overlay(rectile,gauge,[1,1])
        rectile=f.overlay(rectile,gauge,[11,1])
        f.printFrame(rectile)"""
    except KeyboardInterrupt:
        quit()

'''

