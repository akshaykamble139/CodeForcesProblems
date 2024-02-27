t = int(input())

import math

while t > 0:
    t -= 1
    n = int(input())
    if n % 2 == 0 and int(math.sqrt(n // 2)) ** 2 == n // 2:
        print("YES")
    elif n % 4 == 0 and int(math.sqrt(n // 4)) ** 2 == n // 4:
        print("YES")
    else:
        print("NO")
