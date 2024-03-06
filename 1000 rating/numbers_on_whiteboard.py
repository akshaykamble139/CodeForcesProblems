t = int(input())

# 1 2 3 4
# 1 3 3
# 1 3
# 2

while t > 0:
    t -= 1
    n = int(input())
    if n == 2:
        print(2)
        print(1, 2)
    else:
        print(2)
        arr = [a for a in range(1, n+1)]
        i = n-1
        a = arr[i]
        b = arr[i-2]
        arr[i-2] = -1
        while (i > 0) and (a != b or (a == b and a != 2)):
            print(b, a)
            g = b
            if arr[i-1] == -1:
                b = arr[i-2]
                i -= 1
            else:
                b = arr[i-1]
            a = (a + g) // 2
            i -= 1

        print(b, a)
