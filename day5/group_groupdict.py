import re
txt = re.search(r'([A-Za-z0-9])\1+',input())
if txt:
    print (txt.group(1))
else:
    print (-1)