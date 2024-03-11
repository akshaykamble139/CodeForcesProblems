import math

t = int(input())

for _ in range(t):
    word = [int(a) for a in input().split()]
    a = min(word)
    b = max(word)
    ans = 0
    if b % a == 0:
        ans = b * (b // a)
    else:
        g = math.gcd(a, b)
        ans = b * (a // g)
    print(ans)