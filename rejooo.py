ni=int(input())
flag=0

l1=[]
ls=list(map(int,input().split()))
for i in range(0,len(ls)):
   if(ls[i]==i):
      temp=ls[i]
      flag=1
      l1.append(temp)
      l1=sorted(l1)
print(*l1)
if(flag==0):
   print("-1")
