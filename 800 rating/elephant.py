n = int(input())

count = 0
if n<=5:
    count = 1
else:
    count = int(n/5)
    if n - count * 5 > 0:
        count += 1

print(count)