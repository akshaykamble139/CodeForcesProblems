arr = [int(a) for a in input().split()]

n = arr[0]
m = arr[1]


if m%n == 0:
    if m == n:
        print(0)
    else:
        mul = m//n
        count = 0
        while mul%3 == 0:
            mul /= 3
            count += 1

        while mul%2 == 0:
            mul /= 2
            count += 1

        if mul != 1:
            print(-1)
        else:
            print(count)
else:
    print(-1)