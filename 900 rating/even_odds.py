arr = [int(a) for a in input().split()]

n = arr[0]
i = arr[1]

if n % 2 == 0:
    if i > n/2:
        even = 2 * (i - (n//2))
        print(even)
    else:
        odd = 2 * i - 1
        print(odd)
else:
    if i > n//2 + 1:
        even = 2 * (i - (n // 2 + 1))
        print(even)
    else:
        odd = 2 * i - 1
        print(odd)