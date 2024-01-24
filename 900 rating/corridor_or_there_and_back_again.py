t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    ans = 2 * 10 ** 9
    for i in range(n):
        temp = [int(a) for a in input().split()]
        d = temp[0]
        s = temp[1]
        ans = min(ans, d + (s-1)//2)

    print(ans)
