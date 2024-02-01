t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    is_in_descending_order = True
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            is_in_descending_order = False
            break

    if is_in_descending_order:
        print("NO")
    else:
        print("YES")
