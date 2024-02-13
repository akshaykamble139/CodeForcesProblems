n = int(input())

# n*(n+1)/2
#1 2 3
# n*1 + (n-1)*2 + (n-3)*3
# 3 4
ans = 0
for i in range(n):
    if i == 0:
        ans += n
    else:
        ans += i*(n-i)

print(ans)
