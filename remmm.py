A=int(input())
B=list(map(int,input().split()))
a1=0
for a in range(len(B)-2):
    for y in range(a+1,len(B)-1):
        for z in range(b+1,len(B)):
            if B[a]<B[b]<B[z] and a<b<z:
                a1=a1+1
print(a1)
