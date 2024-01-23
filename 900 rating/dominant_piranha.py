t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    largest = max(arr)
    largest_count = arr.count(largest)
    if largest_count == n:
        print(-1)
    else:
        for i in range(n):
            if arr[i] == largest:
                if (i-1>=0 and arr[i-1] < largest) or (i+1<n and arr[i+1] < largest):
                    print(i+1)
                    break