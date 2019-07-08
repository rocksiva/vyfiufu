si=int(input())
sh=[int(i) for i in input().split()]
a=0
for ka in range(si):
   for j in range(ka):
      if sh[j]<sh[ka]:
         a+=sh[j]
print(a) 
