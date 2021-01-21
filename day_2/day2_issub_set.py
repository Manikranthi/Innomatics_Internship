n=int(input())
for i in range(n):
  b=int(input())
  l1=set(map(int,input().split()))
  c=int(input())
  l2=set(map(int,input().split()))
  if (l1.issubset(l2)):
    print("True")
  else:
    print("False")  