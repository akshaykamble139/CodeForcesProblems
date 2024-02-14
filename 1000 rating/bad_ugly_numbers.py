t = int(input())

while t>0:
    t -= 1
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print("2" + "3"*(n-1))