t = int(input())

while t>0:
    t -= 1
    n = int(input())
    total = n*(n+1)//2
    deduct = 0
    multiple = 1
    while multiple<=n:
        deduct += 2*multiple
        multiple *= 2

    print(round(total) - deduct)