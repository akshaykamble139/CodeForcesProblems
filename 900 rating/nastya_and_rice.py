t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    a = arr[1]
    b = arr[2]
    c = arr[3]
    d = arr[4]

    low = n*(a-b)
    high = n*(a+b)

    if high < c - d or c + d < low:
        print("No")
    else:
        print("Yes")
