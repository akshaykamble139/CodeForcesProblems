t = int(input())

while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    x = word[0]
    y = word[1]

    arr = [int(a) for a in input().split()]
    a = arr[0]
    b = arr[1]

    if x == 0 and y == 0:
        print(0)
    else:
        low = min(x,y)
        high = max(x,y)
        g = (high-low)*a
        if low*b > 2*low*a:
            g += 2*low*a
        else:
            g += low*b
        print(g)
