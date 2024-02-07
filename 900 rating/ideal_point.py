t = int(input())

while t>0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    seg = []
    lower = 0
    higher = 60
    while n>0:
        n -= 1
        arr = [int(a) for a in input().split()]
        l = arr[0]
        r = arr[1]
        if l<=k<=r:
            if l>lower:
                lower = l
            if r<higher:
                higher = r
            seg.append((l,r))

    if len(seg) > 0 and lower==higher:
        print("YES")
    else:
        print("NO")

