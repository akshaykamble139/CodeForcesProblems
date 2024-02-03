t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    least = min(arr)
    highest = max(arr)
    if least == highest:
        print(n*(n-1))
    else:
        low = 0
        high = 0
        for i in range(n):
            if least == arr[i]:
                low += 1
            if highest == arr[i]:
                high += 1

        print(2*low*high)
