t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    i = 0
    while i<n and arr[i] == 0:
        i += 1
    ans = 0
    for j in range(i,n-1):
        ans += arr[j]
        if arr[j] == 0:
            ans += 1

    print(ans)
