t = int(input())
import math
while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]

# n = 10
# 1 1 1 1 1 1 1 1 1 1 sum => 10
# 1 2 2 2 2 2 2 2 2 2 sum =>
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
    n = arr[0]
    k = arr[1]
    if n%k == 0:
        print(1)
    else:
        if n == 1:
            print(k)
        else:
            c = math.floor((n+k-1)/k)
            k *= c
            print(math.floor((k+n-1)/n))
