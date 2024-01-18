arr = [int(a) for a in input().split()]

n = arr[0]
m = arr[1]

count = 0

while n > 0:
    n -= 1
    count += 1
    if count % m == 0:
        n += 1

print(count)