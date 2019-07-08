siv,sha=input().split()
r=abs(len(siv)-len(sha))
for i in range(len(siv)):
    if len(sha)==1 and sha[i] in siv:
        break
    if siv[i]!=sha[i]:
        r+=1
print(r)
