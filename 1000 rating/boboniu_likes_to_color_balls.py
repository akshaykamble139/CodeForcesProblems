t = int(input())

while t > 0:
    t -= 1
    arr = [int(a) for a in input().split()]
    r = arr[0]
    g = arr[1]
    b = arr[2]
    w = arr[3]
    if r%2 + g%2 + b%2 + w%2 <= 1:
        print("Yes")
    elif r>0 and g>0 and b>0 and (r-1)%2 + (g-1)%2 + (b-1)%2 + (w+1)%2 <= 1:
        print("Yes")
    else:
        print("No")
