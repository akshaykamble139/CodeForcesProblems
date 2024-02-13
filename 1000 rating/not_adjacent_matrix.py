t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        curr = 1
        arr = []
        for i in range(n):
            arr.append([])
            for j in range(n):
                arr[i].append(0)

        for b in [0,1]:
            for i in range(n):
                for j in range(n):
                    if (i+j)%2 == b:
                        arr[i][j] = curr
                        curr += 1

        for i in range(0, n):
            print(" ".join([str(b) for b in arr[i]]))
