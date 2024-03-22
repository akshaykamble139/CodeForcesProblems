t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(a) for a in input().split()]
    arr.sort()
    print(arr[n]-arr[n-1])
    # 0 1 2 3 4 5
    # n = 3

