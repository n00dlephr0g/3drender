import math as m
import vectors as v
import os




def vertexSphere(bounds1,bounds2,resolution):
    step=1/resolution
    points=[]
    range1=v.numRange(bounds1[0]+0.03,bounds1[1],step)
    range2=v.numRange(bounds2[0],bounds2[1],step)
    for s in range1:
        for t in range2:
            point=sphere(1,[0,0,0],s,t)
            try:
                if point!=points[-1]:
                    points.append(point)
            except:
                points.append(point) 
    return points


def sphere(r,pos,s,t):
    x=r*m.sin(s)*m.cos(t)+pos[0]
    y=r*m.sin(t)*m.sin(s)+pos[1]
    z=r*m.cos(s)+pos[2]
    n=v.minus([x,y,z],[pos[0],pos[1],pos[2]])
    return[x,y,z,n]


def cube(point1,point2,direction):
    out=[]
    l=v.mag(v.minus(point1,point2))
    dir1=v.multiply(v.unit(direction),l)
    dir2=v.multiply(v.unit(v.minus(point2,point1)),l)
    dir3=v.multiply(v.unit(v.cross(dir1,dir2)),l)
    dir12=v.add(dir1,dir2)
    dir13=v.add(dir1,dir3)
    dir23=v.add(dir2,dir3)
    dir123=v.add(dir12,dir3)
    orthogonals=[dir1,dir2,dir3]
    diagonals=[dir23,dir13,dir12,dir123]
    corners=[point1,v.add(point1,dir123)]
    index=0
    for c in range(0,2):
        for o in range(0,3):
            for d in range(0,3):
                if o==d:
                    continue
                else:
                    out.append([])
                    out[index].append(corners[c])
                    out[index].append(v.add(point1,orthogonals[o]))
                    out[index].append(v.add(point1,diagonals[d]))
                    index=index+1
    return out
        
    

def genMesh(points):
    out=[]
    bound=range(0,len(points))
    
    return out

        
def desmosPoints(points):
    for i in range(0,len(points)):
        out=f"({points[i][0]},{points[i][1]},{points[i][2]})"
        print(out)


