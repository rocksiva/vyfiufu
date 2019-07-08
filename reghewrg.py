import math
f,z=map(int,input().split())
g=[]
b=list(map(int,input().split()))
for j in range(0,z):
    v,h=map(int,input().split())
    c.append([v,h])
for j in g:
    n=j[0]-1
    m=j[1]-1
    print(math.gcd(b[n],b[m]))
