t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    res = arr[0]
    for i in range(1,n):
        res &= arr[i]

    print(res)
