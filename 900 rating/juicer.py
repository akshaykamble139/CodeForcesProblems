word = [int(a) for a in input().split()]

n = word[0]
b = word[1]
d = word[2]

arr = [int(a) for a in input().split() if int(a) <= b]

current = 0
count = 0

for a in arr:
    current += a
    if current > d:
        count += 1
        current = 0

print(count)