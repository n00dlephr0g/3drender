import math as m
import time as t
import elements as e
import frames as f
import player as p
import vectors as v
import raytrace as rt
import objects as o
import level as l
import os

init=True
#define initial position
pos0 = [0,0,0]
#define initial direction
angDir0 = [0,0]
direction= [0,1,0]
mesh=o.cube([0,-0.5,-0.5],[0,0.5,-0.5],[0,0,1])
distance=3


while True:
    try:
        p.controlPlayer(pos0, angDir0, 2,3,0.02,init)
        init=False
        print('\n')
        frame=rt.castRays([25,20],p.pos,p.direction,mesh,distance,90)
        frame=f.genAsciiFrame(frame)
        os.system('cls')
        print("position: ",v.roundVec(p.pos,2),"\ndirection: ", v.roundVec(p.direction,2))
        f.printFrame(frame)
    except KeyboardInterrupt:
        quit()



