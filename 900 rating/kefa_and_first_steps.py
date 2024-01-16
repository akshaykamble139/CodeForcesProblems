n = int(input())
arr = [int(a) for a in input().split()]

max_count = 1
start_index = 0
curr_count = 1
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        curr_count += 1
        if curr_count > max_count:
            max_count = curr_count
    else:
        start_index = i
        curr_count = 1

print(max_count)
