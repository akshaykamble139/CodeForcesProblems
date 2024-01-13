arr = [int(a) for a in input().split()]

a = arr[0]
b = arr[1]

low = 0
high = 0
if a>b:
    low = b
    high = a
else:
    low = a
    high = b
distinct = low
same = 0
if high - low > 1:
    same += int((high - low)/2)

print(f"{distinct} {same}")
