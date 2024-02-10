word = [int(a) for a in input().split()]

n = word[0]
m = word[1]
if n == m:
    print(n)
elif n == 1:
    print(-1)
elif n == 2:
    if m == 2:
        print("2")
    else:
        print(-1)
else:
    if n - n//2 >= m:
        t = n//2
        if n%2 == 1:
            t += 1
        if t % m == 0:
            print(t)
        else:
            print(m*(t//m + 1))
    elif n//2 < m <= n:
        print(m)
    else:
        print(-1)