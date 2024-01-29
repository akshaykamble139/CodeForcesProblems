t = int(input())

while t > 0:
    t -= 1
    word = [a for a in input().split()]
    x1 = word[0]
    p1 = int(word[1])
    if len(x1) > 1:
        p1 += len(x1) - 1
        x1 = float(x1[0] + "." + x1[1:])
    else:
        x1 = float(x1)

    word = [a for a in input().split()]
    x2 = word[0]
    p2 = int(word[1])
    if len(x2) > 1:
        p2 += len(x2) - 1
        x2 = float(x2[0] + "." + x2[1:])
    else:
        x2 = float(x2)

    if p1 == p2:
        if x1 == x2:
            print("=")
        elif x1 > x2:
            print(">")
        else:
            print("<")
    elif p1 > p2:
        print(">")
    else:
        print("<")
