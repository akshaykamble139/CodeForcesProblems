t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    if a == 0 and c == 0:
        print(0)
    elif a == 0 or c == 0:
        print(1)
    elif a*d == c*b:
        print(0)
    elif a*d % (c*b) == 0 or c*b % (a*d) == 0:
        print(1)
    else:
        print(2)
