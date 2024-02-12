t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]

    A = arr[0]
    B = arr[1]
    if B == 1:
        print("NO")
    else:
        z = 3*A*B
        x = A*(3*B-1)
        y = z - x
        print("YES")
        print(x, y, z)