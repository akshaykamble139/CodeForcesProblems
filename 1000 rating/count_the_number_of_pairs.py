t = int(input())

while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    s = input()
    dict = {}
    for a in s:
        if a.lower() in dict:
            if a.lower() == a:
                dict[a.lower()][0] += 1
            else:
                dict[a.lower()][1] += 1
        else:
            dict[a.lower()] = [0, 0]
            if a.lower() == a:
                dict[a.lower()][0] += 1
            else:
                dict[a.lower()][1] += 1

    ans = 0
    ops = 0
    for key,v in dict.items():
        low = min(v)
        high = max(v)
        ans += low
        if ops < k:
            new = min(k-ops,(high-low)//2)
            ops += new
            ans += new

    print(ans)
