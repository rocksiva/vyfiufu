riii = int(input())
number = sorted(input().split(), reverse=True)
temp = ''
for i in number:
    temp += i
print(int(temp))
