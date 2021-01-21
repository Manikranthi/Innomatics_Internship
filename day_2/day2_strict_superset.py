l1=set(map(int,input().split()))
n=int(input())
l2=[]
for i in range(n):
  l2.append(set(map(int,input().split())))
for k in l2:
  if (k.issubset(l1)):
    j=1
  else:
    j=0
    break
if(j==1):
  print("True")
else:
  print("False")    