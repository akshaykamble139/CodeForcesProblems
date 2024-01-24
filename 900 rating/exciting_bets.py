t = int(input())
from math import gcd

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    a = arr[0]
    b = arr[1]
    if a == b:
        print("0 0")
    else:
        g = abs(a-b)
        moves = min(a%g, (g-a)%g)
        print(f"{g} {moves}")