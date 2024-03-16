t = int(input())
# n-1 n-2 n-3 n-4 n-5 n-4 n-3 n-2 n-1
for _ in range(t):
    n = int(input())
    perm = []
    ans = [0] * n
    dict = {}
    for _ in range(n):
        d = [int(a) for a in input().split()]
        perm.append(d)
        for i in range(n-1):
            if i in dict:
                dict[i].append(d[i])
            else:
                dict[i] = [d[i]]
    ans = []
    for i in range(n-1):
        v = dict[i]
        h = max(v)
        l = min(v)
        c = v.count(h)
        if len(ans) == 0:
            if c == n-1:
                ans.append(h)
                ans.append(l)
            else:
                ans.append(l)
                ans.append(h)
        else:
            prev = ans[-1]
            y = [i for i in v if i != prev][0]
            ans.append(y)

    print(*ans)

