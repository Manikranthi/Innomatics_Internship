k=int(input())
l1=set(map(int,input().split())) 
n=int(input())
for i in range(n):
  a=input()
  opp=a.split()
  
  if (opp[0]=='pop'):
    l1.pop()
  if (opp[0]=='discard'):
    l1.discard(int(opp[1]))
  if (opp[0]=='remove'):
    l1.remove(int(opp[1])) 
print(sum(l1))
