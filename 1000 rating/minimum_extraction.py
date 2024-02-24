t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    if n == 1:
        print(arr[0])
    else:
        arr.sort()
        a = arr[0]
        for i in range(n-1):
            a = max(a, arr[i+1]-arr[i])

        print(a)