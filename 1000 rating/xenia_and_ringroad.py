word = [int(a) for a in input().split()]

n = word[0]
m = word[1]

arr = [int(a) for a in input().split()]

total = arr[0] - 1

for i in range(1, m):
    total += ((arr[i] - arr[i-1] + n) % n)

print(total)