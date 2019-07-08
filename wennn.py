number1=int(input())
list1=list(map(int,input().split()))[:number1]
rev=0
list1.sort(reverse=True)
for i in l1:
  rev=rev*10+i
print(rev)
