t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    a = arr[1]
    b = arr[2]
    s = input()
    m = 1
    prev = s[0]
    for c in s[1:]:
        if c != prev:
            m += 1
            prev = c

    ans = n*a + max(n*b, b*((m//2)+1))
    print(ans)