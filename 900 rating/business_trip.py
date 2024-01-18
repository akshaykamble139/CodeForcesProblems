k = int(input())
arr = [int(a) for a in input().split()]

if k == 0:
    print(0)
else:
    arr.sort()
    sum = 0
    count = 0
    for a in arr[::-1]:
        sum += a
        count += 1
        if sum >= k:
            break
    if sum < k:
        print(-1)
    else:
        print(count)
