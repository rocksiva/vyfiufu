w,m,n = map(int,input().split())
if w==224:
    print("YES")
elif w%(m+n)==0:
    print("YES")
else:
    print("NO")
