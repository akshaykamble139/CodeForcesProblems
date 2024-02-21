t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    c_0 = 0
    c_1 = 0
    c_2 = 0
    for a in arr:
        rem = a%3
        if rem == 0:
            c_0 += 1
        if rem == 1:
            c_1 += 1
        if rem == 2:
            c_2 += 1

    ans = 0
    if c_0 == c_1 == c_2:
        print(ans)
    else:
        c = [c_0, c_1, c_2]
        while min(c) != n//3:
            for i in range(3):
                if c[i] > n//3:
                    ans += 1
                    c[i] -= 1
                    c[(i+1)%3] += 1

        print(ans)


