t = int(input())

from math import gcd


def result():
    n = int(input())
    arr = [int(a) for a in input().split()]
    even = [a for a in arr if a%2 == 0]
    odd = [a for a in arr if a%2 == 1]
    ans = int(len(even) * (len(even)-1) / 2 + len(even) * len(odd))
    for i in range(len(odd)):
        for j in range(i+1,len(odd)):
            val = gcd(odd[i],odd[j])
            if val > 1:
                ans += 1

    print(ans)


while t > 0:
    t -= 1
    result()
