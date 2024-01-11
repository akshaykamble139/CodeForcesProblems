n = int(input())
arr = [int(a) for a in input().split()]

min_val = 0
for i in range(0,n):
    if arr[min_val] >= arr[i]:
        min_val = i

max_val = 0
for i in range(0,n)[::-1]:
    if arr[max_val] <= arr[i]:
        max_val = i

# print(f"max = {max_val}")
# print(f"min = {min_val}")

if arr[min_val] == arr[max_val]:
    print(0)
elif max_val < min_val:
    print(max_val + n-1 - min_val)
else:
    print(max_val - min_val + n - 2)
