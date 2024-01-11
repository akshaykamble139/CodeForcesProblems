n = int(input())

first = [int(a) for a in input().split()]
second = [int(a) for a in input().split()]

arr = [a for a in range(1,n+1)]
for a in first[1::]:
    if a in arr:
        arr.remove(a)

for a in second[1::]:
    if a in arr:
        arr.remove(a)

if len(arr) == 0:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
