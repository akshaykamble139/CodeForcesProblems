t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    required = 0
    current = 0
    has_enough = True
    for i in range(n):
        required += i
        current += arr[i]
        if current < required:
            has_enough = False
            break
    if has_enough:
        print("YES")
    else:
        print("NO")
