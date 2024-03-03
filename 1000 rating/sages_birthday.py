n = int(input())

arr = [int(a) for a in input().split()]

temp = arr
temp.sort()
print((n-1)//2)

ans = []
i = 0
j = n//2

while i<n//2 and j<n:
    ans.append(temp[j])
    ans.append(temp[i])
    i += 1
    j += 1

if j<n:
    ans.append(temp[j])

print(*ans)



# 0 1 2 3
# 0 1 2 3 4