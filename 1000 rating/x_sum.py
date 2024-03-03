import collections
t = int(input())

d_x = [1, 1, -1, -1]
d_y = [1, -1, 1, -1]
while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    m = word[1]
    arr = []
    for _ in range(n):
        temp = [int(a) for a in input().split()]
        arr.append(temp)

    ans = 0
    x = collections.defaultdict(int)
    y = collections.defaultdict(int)

    for i in range(n):
        for j in range(m):
            x[i+j] += arr[i][j]
            y[i-j] += arr[i][j]

    for i in range(n):
        for j in range(m):
            ans = max(ans, x[i+j] + y[i-j] - arr[i][j])

    print(ans)
