t = int(input())

while t > 0:
    t -= 1
    arr = [int(x) for x in input().split()]
    arr.sort()
    a = arr[0]
    b = arr[1]
    c = arr[2]
    if a == b == c:
        print("YES")
    elif b%a == 0 and c%a == 0:
        if c//a == 3:
            if b//a == 2 or b//a == 1:
                print("YES")
            else:
                print("NO")
        elif c//a == 4:
            if b//a == 1:
                print("YES")
            else:
                print("NO")
        elif c//a > 2 or b//a > 2:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")




