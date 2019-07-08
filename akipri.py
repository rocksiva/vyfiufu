Num1=int(input())
n0=list(map(int,input().split()))
for ka in range(len(n0)):
    if n0.count(n0[ka])==1:
        print(n0[ka])
