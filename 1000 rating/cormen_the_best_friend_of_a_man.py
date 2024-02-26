word = [int(a) for a in input().split()]

n = word[0]
k = word[1]

arr = [int(a) for a in input().split()]

count = 0
ans = [0] * n

i = 0
while i<n-1:
    c = arr[i]
    d = arr[i+1]
    # print(f"i = {i} c = {c} d = {d}")
    diff = 0
    if c+d<k:

        diff = k - c - d
        count += diff
        d += diff
    arr[i] = c
    arr[i+1] = d
    i += 1

# if i == n-1:
#     ans.append(arr[i])

print(count)
print(" ".join([str(a) for a in arr]))
