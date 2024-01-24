n = int(input())

arr = [int(a) for a in input().split()]

count = 0
pos = 0
neg = 0
zero = 0
for a in arr:
    if abs(a) == 1:
        if a > 0:
            pos += 1
        else:
            neg += 1
    else:
        if a>1:
            count += a-1
            pos += 1
        elif a == 0:
            zero += 1
        else:
            count += (-1-a)
            neg += 1

# print(f"count = {count}")
if zero == 0:
    if neg % 2 == 0:
        print(count)
    else:
        print(count+2)
else:
    print(count+zero)
