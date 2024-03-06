n = int(input())

arr = [int(a) for a in input().split()]

total = sum(arr)
ans = 0
for a in range(1,6):
    d = (a + total) % (n+1)
    if d != 1:
        ans += 1

print(ans)