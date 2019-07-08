import math
a,p=map(int,input().split())
g=[]
b=list(map(int,input().split()))
for j in range(0,p):
    k,r=map(int,input().split())
    c.append([k,r])
for j in g:
    i=j[0]-1
    ii=j[1]-1
    print(math.gcd(b[i],b[ii]))
