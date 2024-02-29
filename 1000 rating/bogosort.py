t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    if n == 1:
        print(arr[0])
    else:
        arr.sort(reverse=True)
        print(*arr)



