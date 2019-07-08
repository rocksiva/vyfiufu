kan,jan=map(str,input().split())
s=0
if len(kan)>len(jan):
  kan,jan=jan,kan
i=0
while i<len(kan):
  s+=(ord(jan[i])-ord(kan[i]))
  i+=1
for i in range(i,len(jan)):
  s+=ord(jan[i])-ord('a')+1
print(s)
