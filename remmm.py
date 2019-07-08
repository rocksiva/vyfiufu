    
x=int(input())
arr=list(map(int,input().split()))
y=0
for i in range(0,x-2):
	for j in range(1,x-1):
		for k in range(2,x):
			if((arr[i] < arr[j]) and (arr[j] < arr[k])):
				y+=1
print(y)
