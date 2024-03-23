t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(a) for a in input().split()]
    if n == 1 or n == 2:
        print("YES")
    else:
        arr = [1000_000_000_000] + arr + [1000_000_000_000]
        i = 1
        count = 0
        # print(arr)
        while i < n+1:
            if arr[i-1]>arr[i]:
                if arr[i] > arr[i+1]:
                    i+=1
                    continue
                l = arr[i]
                while i<n+1 and l == arr[i]:
                    i+=1
                # print(f"count = {count} l = {l} arr[{i}] = {arr[i]}")
                if l < arr[i]:
                    count += 1
            else:
                i += 1

        if count == 1:
            print("YES")
        else:
            print("NO")






