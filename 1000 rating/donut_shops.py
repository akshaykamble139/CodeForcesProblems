t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    first = -1
    second = -1
    if a < c:
        each_donut_cost = c/b
        first = 1
        if each_donut_cost < float(a):
            second = b
    else:
        second = b

    print(f"{first} {second}")
