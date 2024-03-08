word = [int(a) for a in input().split()]
arr = [int(a) for a in input().split()]

n = word[0]
a = word[1]


ans = 0
i = a-1
if arr[i] == 1:
    ans = 1
distance = 1
while i + distance < n and i-distance >= 0:
    if arr[i+distance] == 1 and arr[i-distance]:
        ans += 2
    distance += 1

while i + distance < n:
    if arr[i + distance] == 1:
        ans += 1
    distance += 1

while i - distance >= 0:
    if arr[i - distance]:
        ans += 1
    distance += 1

print(ans)
