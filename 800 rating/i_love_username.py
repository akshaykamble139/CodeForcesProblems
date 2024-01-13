n = int(input())
low = 20000
high = 0
arr = [int(a) for a in input().split()]

count = 0
for a in arr:
    if low == 20000 and high == 0:
        low = a
        high = a
    else:
        if a < low:
            low = a
            count += 1
        if a > high:
            high = a
            count += 1

print(count)
