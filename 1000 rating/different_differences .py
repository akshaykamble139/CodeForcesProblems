t = int(input())


def helper(f, k):
    return [(i + 2 if i < f - 1 else 1) for i in range(k)]


for _ in range(t):
    word = [int(a) for a in input().split()]
    k = word[0]
    n = word[1]
    ans = 1
    for f in range(1, k):
        d = helper(f, k - 1)
        # print(f"for loop d = {d}")
        if sum(d) <= n - 1:
            ans = f
    res = [1]
    d = helper(ans, k - 1)
    # print(f"after d = {d}")
    for x in d:
        res.append(res[-1] + x)
    print(*res)