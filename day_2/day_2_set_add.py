n =int(input())
arr=[]
for i in range(0,n):
  arr.append(input())
l1=set()
for i in arr:
  l1.add(i)
print(len(l1)) 
   