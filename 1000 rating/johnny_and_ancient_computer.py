t = int(input())


def solve(a,b):
    if a == b:
        return 0
    elif a % b != 0 and b % a != 0:
        return -1
    if a>b:
        t = a
        a = b
        b = t
    r = a
    while r%2 == 0:
        r //= 2

    g = b
    while g%2 == 0:
        g //= 2

    if g!= r:
        return -1

    ans = 0
    b //= a

    while b>=8:
        b //= 8
        ans += 1
    # print(f"first ans = {ans} b = {b}")
    while b>=4:
        b //= 4
        ans += 1
    # print(f"second ans = {ans} b = {b}")
    while b>1:
        b //= 2
        ans += 1
    # print(f"last ans = {ans} b = {b}")
    return ans


for _ in range(t):
    word = [int(a) for a in input().split()]
    first = word[0]
    second = word[1]
    print(solve(first,second))


