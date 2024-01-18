q = int(input())

while q > 0:
    q -= 1
    n = int(input())
    if n < 2020:
        print("NO")
    elif (n%2020 == 0) or (n%2021 == 0) or (n%4041 == 0):
        print("YES")
    else:
        # 2020 * x + 2021 * y = n
        while n > 2020 and n % 2020 != 0:
            n -= 2021
        while n > 0 and n % 2020 != 0:
            n -= 2020
        n = n % 2020

        if n == 0:
            print("YES")
        else:
            print("NO")
