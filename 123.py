kan=int(input())
l1=[]
l2=[]
l1=list(input().split())
for i in range(0,len(l1)):
    if (l1.count(l1[i])>=2):
        l2.append(l1[i])
if(len(l2)==0):
    print("unique")
else:
    print(' '.join(sorted(set(l2))))
