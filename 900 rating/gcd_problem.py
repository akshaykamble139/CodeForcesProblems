t = int(input())

while t>0:
    t -= 1
    n = int(input())
    if n%2 == 0:
        c = 1
        a = (n - 1) // 2
        b = n - c - a
    elif n%4 == 1:
        c = 1
        a = n // 2 - 1
        b = n - c - a
    else:
        c = 1
        a = n//2 - 2
        b = n - c - a

    print(f"{a} {b} {c}")
