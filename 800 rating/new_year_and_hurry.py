arr = [int(a) for a in input().split()]
n = arr[0]
k = arr[1]

total = 60 * 4
total -= k

count = 0

while total > 0 and count < n:
    if total - 5*(count+1) < 0:
        break
    else:
        count += 1
        total -= 5*count
        # print(f"count = {count} total = {total}")

print(count)