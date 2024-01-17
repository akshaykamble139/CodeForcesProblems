q = int(input())

while q > 0:
    q -= 1
    n = int(input())
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            print("YES")
            break

    if n == 1:
        print("NO")