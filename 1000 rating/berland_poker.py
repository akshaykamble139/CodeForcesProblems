t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    m = arr[1]
    k = arr[2]
    if m == 0:
        print(0)
    else:
        each = n//k
        if each >= m:
            print(m)
        else:
            a1 = min(m, each)
            a2 = (m-a1+k-2) // (k-1)
            print(a1 - a2)