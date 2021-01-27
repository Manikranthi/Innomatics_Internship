import re
text=input()
match=re.findall(r'(?<=[^aeiouAEIOU ])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU ])',text)
if (match):
    for i in match:
        if (i):
            print(i)
else:
    print(-1)