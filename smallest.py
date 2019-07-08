from itertools import combinations
a,s=input().split()
s=int(sk)
l=[]
pd=combinations(a,len(a)-s)
for i in list(pd):
  l.append("".join(i))
print(min(l))
