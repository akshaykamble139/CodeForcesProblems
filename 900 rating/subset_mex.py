t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    count = [0 for i in range(101)]
    for a in arr:
        count[a] += 1

    ans = 0
    for i in range(101):
        if count[i] == 0:
            ans += i
            break
    for i in range(101):
        if count[i] <= 1:
            ans += i
            break

    print(ans)