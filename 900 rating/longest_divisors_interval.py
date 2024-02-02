t = int(input())

while t>0:
    t -= 1
    n = int(input())
    if n == 1:
        print(1)
    else:
        for i in range(1,n+2):
            if n%i != 0:
                print(i-1)
                break

