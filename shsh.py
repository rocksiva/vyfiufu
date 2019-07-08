q= int(input())
y=[]
for m in range(0,q):
 chr=input()
 y.append(chr)
n=[]
for m in zip(*y):
 if(m.count(m[0])==len(m)):
  n.append(m[0])
 else:
  break
print(''.join(n))
© 2019 GitHub, Inc.
