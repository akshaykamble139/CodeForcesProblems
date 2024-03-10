t = int(input())

for _ in range(t):
    a = input()
    b = input()
    if a == b:
        print(0)
    else:
        n = len(a)
        m = len(b)
        ans = 0
        for l in range(1, min(n,m) + 1):
            for i in range(n - l + 1):
                for j in range(m - l + 1):
                    # print(a[i:i+l] + " " + b[j:j+l])
                    if a[i:i+l] == b[j:j+l]:
                        ans = max(ans, l)

        print(n+m - 2*ans)
