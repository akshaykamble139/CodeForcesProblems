t = int(input())

while t>0:
    t -= 1
    arr = [int(z) for z in input().split()]
    l = arr[0]
    r = arr[1]
    a = arr[2]
    ans = r//a + r%a
    m = (r//a) * a - 1
    if m>=l:
        ans = max(ans, m//a + m%a)

    print(ans)
