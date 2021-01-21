def average(array):
    set1=set()
    for i in range(len(arr)):
        set1.add(arr[i])
    result=sum(list(set1))/len(set1)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)