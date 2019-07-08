si=int(input())
sh=1
while(sh<=si and sh*2<=si):
    sh=sh*2
if(sh==si):
    print("0")
else:    
    print(si-sh)
