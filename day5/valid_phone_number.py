import re
n=int(input())
for i in range(n):
    a=input()
    if(len(str(a))==10):
        y=re.findall(r'^[7-9][0-9]{9}',a)
        if (y):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")