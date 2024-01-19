import math
t = int(input())


def result(x,n,m):
    a = n
    b = m
    if x > 10:
        while x > 0 and a > 0:
            x = int(math.floor(x/2)) + 10
            a -= 1
            # print(f"a = {a} b = {b} x = {x}")

    while x > 0 and b > 0:
        x -= 10
        b -= 1
        # print(f"a = {a} b = {b} x = {x}")

    if x>0:
        print("NO")
    else:
        print("YES")


while t > 0:
    t -= 1
    arr = [int(a) for a in input().split()]
    x = arr[0]
    n = arr[1]
    m = arr[2]
    result(x,n,m)

