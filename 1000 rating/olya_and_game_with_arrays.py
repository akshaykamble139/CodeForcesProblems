t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    m = []
    arr = []
    for _ in range(n):
        m.append(int(input()))
        arr.append([int(a) for a in input().split()])

    for l in arr:
        l.sort()

    second_min_sum = sum(l[1] for l in arr)
    lowest_min = min(l[0] for l in arr)

    ans = max(second_min_sum + lowest_min - l[1] for l in arr)
    print(ans)