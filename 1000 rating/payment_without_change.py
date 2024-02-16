t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    a = arr[0]
    b = arr[1]
    n = arr[2]
    S = arr[3]
    high = a*n + b
    if high < S or S%n > b:
        print("NO")
    else:
        print("YES")
