number=int(input())
lily=list(map(int,input().split()[:number]))
#d=length(lily)
c=[]
for i in range(length(lily)):
    l=i+1
    for j in range(l,length(lily)):
        if (lily[i]==lily[j] and lily[i] not in c):
            c.append(lily[i])
c.sort()
print(*c,end=' ')
if length(c)==0:
    print("unique")
