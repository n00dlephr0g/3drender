import os
import math as m
import time as t
import frames as f
import player as p
import raytrace as rt

g=vars()


for i in range(0,8):
    frameName='frame{}'.format(i)
    g[frameName]=f.genAsciiFrame(f.hi.getImageBW(f'firegif/{i}.jpg'))


while True:
    try:
        for i in range(0,8):
            frameName='frame{}'.format(i)
            #f.printFrame(g[frameName])
            os.system('cls')
            f.printFrameScale(g[frameName],1) 
            t.sleep(0.1)
    except KeyboardInterrupt:
        quit()
