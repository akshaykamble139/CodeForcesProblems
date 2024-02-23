t = int(input())

while t>0:
    t -= 1

    arr = [int(a) for a in input().split()]
    n = arr[0]
    m = arr[1]

    first = "W" + "B"*(m-1)
    print(first)
    for _ in range(n-1):
        print("B"*m)