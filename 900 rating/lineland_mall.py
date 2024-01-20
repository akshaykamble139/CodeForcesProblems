n = int(input())

arr = [int(a) for a in input().split()]

for i in range(n):
    min_val = 10 ** 9
    max_val = -10 ** 9
    if i == 0:
        min_val = arr[1] - arr[0]
        max_val = arr[-1] - arr[0]
    elif i == n-1:
        min_val = arr[-1] - arr[-2]
        max_val = arr[-1] - arr[0]
    else:
        if arr[i] - arr[i-1] < arr[i+1] - arr[i]:
            min_val = arr[i] - arr[i-1]
        else:
            min_val = arr[i+1] - arr[i]

        if arr[i] - arr[0] > arr[-1] - arr[i]:
            max_val = arr[i] - arr[0]
            # print(f"first max {max_val}")
        else:
            max_val = arr[-1] - arr[i]
            # print(f"second max {max_val}")

    print(f"{min_val} {max_val}")



