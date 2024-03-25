t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(a) for a in input().split()]
    bonus = [0]*n
    ans = 0
    for a in arr:
        if a == 0 and len(bonus)>0:
            ans += bonus.pop()
        elif a>0:
            bonus.append(a)
            j = len(bonus) - 1
            while bonus[j] < bonus[j-1]:
                bonus[j], bonus[j-1] = bonus[j-1], bonus[j]
                j -= 1

    print(ans)
