k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

arr = range(1,d+1)
count = 0
for a in arr:
    if a%k != 0 and a%l != 0 and a%m != 0 and a%n != 0:
        count += 1

print(d-count)