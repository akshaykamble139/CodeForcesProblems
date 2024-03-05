t = int(input())

while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    q = word[2]
    arr = [int(a) for a in input().split()]
    l = 0
    ans = 0
    for a in arr:
        if a <= q:
            l += 1
        else:
            if l >= k:
                ans += (l-k+2)*(l-k+1)//2
            l = 0

    if l >= k:
        ans += (l - k + 2) * (l - k + 1) // 2

    print(ans)



