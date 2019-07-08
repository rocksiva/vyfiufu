from itertools import combinations
(number, w) =input().split()
w=int(w)
arr=[]
comb=combinations(number,len(number)-w)
comb=list(comb)
#print(comb)
for i in (comb):
    arr.append("".join(i))
#print(arr)
print(min(arr))
#for i in list(comb):
#    arr.append()
