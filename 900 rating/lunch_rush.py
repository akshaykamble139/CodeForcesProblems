word = [int(a) for a in input().split()]

n = word[0]
k = word[1]

values = []
for i in range(n):
    arr = [int(a) for a in input().split()]
    f = arr[0]
    t = arr[1]
    if t <= k:
        values.append(f)
    else:
        values.append(f-(t-k))

print(max(values))


