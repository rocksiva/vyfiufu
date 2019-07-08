n0=input()
ka=1
for j in range(len(n0)-1):
    si=n0[j]+n0[j+1]
    pr=int(si)
    if pr<=26 and n[j]!="0":
        ka+=1
if ka==3:
    print(ka)
else:
    print(k+(ka-1)//2)
