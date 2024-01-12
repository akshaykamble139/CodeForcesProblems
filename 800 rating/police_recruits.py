n = int(input())
count = 0
police = 0
arr = [int(a) for a in input().split()]

for a in arr:
    if a == -1:
        if police == 0:
            count += 1
        else:
            police -= 1
    else:
        police += a

print(count)

