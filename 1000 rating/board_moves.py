t = int(input())
while t>0:
    t -= 1
    n = int(input())
    if n == 1:
        print(0)
    else:
        k = (n-1)//2
        count = 4 * k * (k+1) * (2*k + 1) // 3

        print(count)