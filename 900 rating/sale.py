word = [int(a) for a in input().split()]
n = word[0]
m = word[1]

arr = [int(a) for a in input().split()]
arr.sort()

tv = 0
money = 0

for a in arr:
    if a <= 0:
        tv += 1
        money -= a
        if tv == m:
            break

print(money)

