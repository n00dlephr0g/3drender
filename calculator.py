import vectors as v
import math as m

p1=[3,-3,0]
p2=[-3,3,3]
p3=[1,-3,3]

v1=v.minus(p2,p1)
v2=v.minus(p3,p1)

l=[0,1,-3]
l0=[3,1,1]

n=v.cross(v1,v2)

print(
    n,
    v.minus(p1,l0),
    v.dot(v.minus(p1,l0),n),
    v.dot(l,n),
    v.multiply(l,60/24)
)