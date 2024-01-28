t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    already_in_ascending = True
    first = arr[0]
    for i in range(1,n):
        if first>arr[i]:
            already_in_ascending = False
            break
        else:
            first = arr[i]

    if already_in_ascending:
        print(0)
    else:
        ans = 2
        if arr[0] == 1 or arr[-1] == n:
            ans = 1
        elif arr[0] == n and arr[-1] == 1:
            ans = 3

        print(ans)