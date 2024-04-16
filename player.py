import vectors as v
import math as m
import time as t
import keyboard as k
import pyautogui as pag
import os

#x is east
#y is north
#z is up-down


def controlPlayer(initPos,initAngDir,speed,sensitivity,tickspeed,init):
    """
    inputs:\n
    initial position (3d vector)\n
    initial angle directions (list of xy angle and z angle)\n
    player speed (real number)\n
    sensitivity (real number)\n
    tickspeed (real number, milliseconds)\n
    outputs:\n
    sets global variables:\n
    current player direction angles\n
    current player direction vector\n
    current player position\n
    """
    global angDir, direction, pos
    if init:
        angDir=initAngDir
        pos=initPos
    direction=v.getDir(initAngDir)
    angIncx=sensitivity*0.001
    angIncy=2*angIncx/3
    sizex,sizey=pag.size()
    centrex=sizex/2-1
    centrey=sizey/2-1
    posInc=speed*(tickspeed+0.12)
    try:
        pag.moveTo(centrex,centrey)
        currx,curry = pag.position()
        t.sleep(tickspeed)
        movex=currx-centrex
        movey=curry-centrey
        direction = v.getDir(angDir)
        dirxy=v.getDir(angDir)
        if k.is_pressed('esc'):
            quit()
        if movex>0:
            angDir[1]=angDir[1]+angIncx*movex
        if movex<0:
            angDir[1]=angDir[1]+angIncx*movex
        if movey>0:
            angDir[0]=angDir[0]-angIncy*movey
        if movey<0:
            angDir[0]=angDir[0]-angIncy*movey
        if angDir[0]>0.49*m.pi:
            angDir[0]=0.49*m.pi
        if angDir[0]<-0.49*m.pi:
            angDir[0]=-0.49*m.pi
        if k.is_pressed('w'):
            pos[0]=pos[0]+posInc*dirxy[0]
            pos[1]=pos[1]+posInc*dirxy[1]
        if k.is_pressed('s'):
            pos[0]=pos[0]-posInc*dirxy[0]
            pos[1]=pos[1]-posInc*dirxy[1]
        if k.is_pressed('a'):
            pos[0]=pos[0]-posInc*dirxy[1]
            pos[1]=pos[1]+posInc*dirxy[0]
        if k.is_pressed('d'):
            pos[0]=pos[0]+posInc*dirxy[1]
            pos[1]=pos[1]-posInc*dirxy[0]
        if k.is_pressed('space'):
            pos[2]=pos[2]+posInc
        if k.is_pressed('shift'):
            pos[2]=pos[2]-posInc
        if k.is_pressed('r'):
            angDir=[0,0]
            pos=[0,0,0]
    except KeyboardInterrupt:
        quit()


def printPlayerPos():
    print(f"position: {v.roundVec(pos,2)}")


def printPlayerDir():
    print(f"direction: {v.roundVec(direction,2)}")





