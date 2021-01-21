n = int(input())
l1=[]
for i in range(0,n):
  l2=[]
  l2.append(input())
  l2.append(float(input()))
  l1.append(l2)
l3=[]
for m in range(0,n):
    if((l1[m][1]) not in l3):
        l3.append((l1[m][1]))
l3.sort()
s_g=l3[1]
l4=[]
for nam in range(0,n):
  if (l1[nam][1]==s_g):
    l4.append(l1[nam][0])
l4.sort()

for k in range(0,len(l4)):
    print(l4[k])