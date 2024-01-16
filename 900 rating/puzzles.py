word = [int(a) for a in input().split()]
n = word[0]
m = word[1]

arr = [int(a) for a in input().split()]

min_diff = 1000
arr.sort()

for i in range(m-n+1):
    diff = arr[i+n-1] - arr[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)