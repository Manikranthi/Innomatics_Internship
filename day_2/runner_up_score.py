def secondmax():
    n = int(input())
    
    arr = list(map(int, input().split()))
    l1=[]
    for i in range(0,len(arr)):
        if(arr[i] not in l1):
            l1.append(arr[i])
    l1.sort()
    print(l1[-2])
secondmax()    