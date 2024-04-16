import math as m


'''
variables that start with c are coordinates.
c = [x,y]

variables that start with p are points.
p = [x,y,z]

variables that start with l are lines
format of lines:
vec = [x0,y0,z0] + t(x,y,z)
line = [x0,y0,z0,x,y,z]

shapes:
    spheres:
        r = radius
        [x0,y0,z0] = centre
        (x-x0)^2 + (y-y0)^2 + (z-z0)^2 = r^2
'''

def mag(vec):
    '''
    inputs:
    vector
    outputs:
    vector magnitude
    '''
    sum = 0
    for i in range(0,len(vec)):
        sum = sum + vec[i]**2
    return m.sqrt(sum)


def unit(vec):
    '''
    inputs:
    vector
    outputs:
    unit vector
    '''
    out=[]
    for i in range(0,len(vec)):
        out.append(vec[i]/mag(vec))
    return out


def add(vec1,vec2):
    '''
    inputs:
    2 vectors
    outputs:
    elentwise addition of the vectors
    '''
    out=[]
    if len(vec1)!=len(vec2):
        raise Exception("vectors are not the same length")    
    for i in range(0,len(vec1)):
        out.append(vec1[i]+vec2[i])
    return out


def minus(vec1,vec2):
    '''
    inputs:
    2 vectors
    outputs:
    elementwise difference of the vectors (vec1-vec2)
    '''
    out=[]
    if len(vec1)!=len(vec2):
        raise Exception("vectors are not the same length")    
    for i in range(0,len(vec1)):
        out.append(vec1[i]-vec2[i])
    return out


def multiply(vec,a):
    '''
    inputs:
    vector
    coefficient
    outputs:
    scalar multiple of vector
    '''
    out=[]
    for i in range(0,len(vec)):
        out.append(vec[i]*a)
    return out


def genVec(p1, p2):
    out=minus(p1,p2)
    return out


def dot(vec1,vec2):
    '''
    inputs:
    2 vectors
    outputs:
    dot product (scalar)
    '''
    out=0
    if len(vec1)!=len(vec2):
        raise Exception("vectors are not the same length")
    for i in range(0,len(vec1)):
        out= out+(vec1[i]*vec2[i])
    return out

def cross(vec1,vec2):
    '''
    inputs:
    2 vectors
    outputs:
    cross product (vector)
    '''
    out=[]
    if len(vec1)!=len(vec2):
        raise Exception("vectors are not the same length")
    out.append(vec1[1]*vec2[2]-vec1[2]*vec2[1])
    out.append(vec1[2]*vec2[0]-vec1[0]*vec2[2])
    out.append(vec1[0]*vec2[1]-vec1[1]*vec2[0])
    return out


def equate(vec1,vec2):
    '''
    inputs:
    2 vectors
    ouputs:
    True if they are same
    False if not
    '''
    n=0
    if len(vec1)!=len(vec2):
        raise Exception("vectors are not the same length")
    for i in range(0,len(vec1)):
        if vec1[i]==vec2[i]:
            n=n+1
    if n==len(vec1):
        return True
    else:
        return


def roundVec(vec,places):
    '''
    input:
    vector
    round to (integer)
    outputs:
    elementwise rounding to places specified
    '''
    out=[]
    for i in range(0,len(vec)):
        out.append(round(vec[i],places))
    return out


def floorVec(vec):
    out=[]
    for i in range(0,len(vec)):
        out.append(m.floor(vec[i]))
    return out


def ceilVec(vec):
    out=[]
    for i in range(0,len(vec)):
        out.append(m.ceil(vec[i]))
    return out


def sameSign2(a,b):
    apositive=a==abs(a)
    bpositive=b==abs(b)
    if apositive==bpositive:
        return True
    else:
        return False


def sameSign3(a,b,c):
    apositive=a==abs(a)
    bpositive=b==abs(b)
    cpositive=c==abs(c)
    if apositive==bpositive:
        if apositive==cpositive:
            return True
    else:
        return False


def lerp(a,b,t):
    p=a*(1-t)+b*t
    return p


def lerpVec(point1,point2,t):
    out=[]
    for i in range(0,len(point1)):
        out.append(lerp(point1[i],point2[i],t))
    return out


def swap2d(vec):
    out=[]
    out.append(vec[1])
    out.append(vec[0])
    return out


def rotate90(vec):
    out=[]
    out.append(-vec[1])
    out.append(vec[0])
    return out


def getDir(angDir):
    '''
    inputs:
    direction angles ([xy, z])
    outputs:
    direction vector (unit vector [z, y, z])
    '''
    out=[]
    zDir=m.sin(angDir[0])
    out.append((1-abs(zDir))*(m.sin(angDir[1])))
    out.append((1-abs(zDir))*(m.cos(angDir[1])))
    out.append(zDir)
    return unit(out)


def getDirxy(angDir):
    '''
    inputs:
    direction angles ([xy, z])
    ouputs:
    direction vector, only x, y (unit vector [x, y])
    '''
    out=[]
    out.append(m.cos(angDir[1]))
    out.append(m.sin(angDir[1]))
    return out


def numRange(l,u,step):
    out=[]
    i=0
    while i*step<u:
        out.append(l+i*step)
        i=i+1
    return out


def sort(vec):
    out=vec
    out.sort()
    return out


def linePlaneDist(position,direction,distance,plane):
    p1=plane[0]
    p2=plane[1]
    p3=plane[2]
    pv1=minus(p2,p1)
    pv2=minus(p3,p1)
    n=unit(cross(pv1,pv2))
    t=(dot(n,p1)-dot(n,position))/dot(n,direction)
    return 1- (t/distance)


def genPlane():
    pass


