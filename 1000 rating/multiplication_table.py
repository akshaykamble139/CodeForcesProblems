word = [int(a) for a in input().split()]
n = word[0]
x = word[1]

if x>n*n:
    print(0)
else:
    ans = 0
    for i in range(2,n+1):
        if x%i == 0 and x//i <= n:
            ans += 1

    if x <= n:
        ans += 1
    print(ans)


