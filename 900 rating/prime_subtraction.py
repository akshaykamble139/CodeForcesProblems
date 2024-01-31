t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    x = arr[0]
    y = arr[1]
    if x-y == 1:
        print("NO")
    else:
        print("YES")