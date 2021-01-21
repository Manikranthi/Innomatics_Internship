student_marks={}
n=int(input())
for i in range(n):
  name_marks=input()
  n1=name_marks.split()
  name=n1[0]
  marks=[float(n1[1]),float(n1[2]),float(n1[3])]
  student_marks[name]=marks
n2=input()
l1=student_marks.get(n2)
a=sum(l1)/3
print("{:.2f}".format(a))