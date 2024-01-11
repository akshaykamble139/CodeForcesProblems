import math
n = int(input())

while n>0:
    n -= 1
    arr = [int(a) for a in input().split()]
    a = arr[0]
    b = arr[1]
    if a % b == 0:
        print(0)
    else:
        count = int(b * (math.floor(a/b)+1)) - a
        print(count)