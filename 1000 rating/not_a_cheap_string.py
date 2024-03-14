t = int(input())

for _ in range(t):
    word = input()
    p = int(input())
    y = [c for c in word]
    y.sort()
    g = [ord(h)-ord('a') + 1 for h in y]
    val = sum(g)

    if val <= p:
        print(word)
    else:
        l = 0
        k = len(g)
        mid = (l+k+1)//2

        while l<k:
            mid = (l+k+1)//2
            # print(f"inside while loop l = {l} k = {k} sum = {sum(g[:mid])}")
            if sum(g[:mid]) == p:
                break
            elif sum(g[:mid]) > p:
                k = mid-1
            else:
                l = mid

        dict = {}
        if l == k and sum(g[:l]) <= p:
            mid = l
        # print(f"l = {l} k = {k} mid = {g[:mid]}")
        # print(sum(g[:mid]))
        for i in range(mid):
            f = y[i]
            if f in dict:
                dict[f] += 1
            else:
                dict[f] = 1

        ans = ""
        for c in word:
            if c in dict:
                ans += c
                dict[c] -= 1
                if dict[c] == 0:
                    dict.pop(c)

        print(ans)





