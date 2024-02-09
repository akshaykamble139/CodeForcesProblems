arr = [int(a) for a in input().split()]

s = arr[0]
n = arr[1]

levels = []
for _ in range(n):
    levels.append([int(a) for a in input().split()])

levels.sort()

power = s
has_defeated_all = True
i = 0

for a in levels:
    if power <= a[0]:
        has_defeated_all = False
        break
    else:
        power += a[1]

if has_defeated_all:
    print("YES")
else:
    print("NO")
