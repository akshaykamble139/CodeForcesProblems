t = int(input())

while t>0:
    t -= 1
    n = int(input())
    r = [int(a) for a in input().split()]
    l = 0
    y = 0
    for a in r:
        l += a
        y = max(y,l)

    m = int(input())
    b = [int(a) for a in input().split()]

    k = 0
    z = 0
    for a in b:
        k += a
        z = max(z, k)

    ans = y + z

    print(ans)

