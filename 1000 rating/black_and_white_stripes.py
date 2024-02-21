t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    k = arr[1]
    s = input()
    count = 0
    if s.find("B"*k) != -1:
        print(count)
    elif n == 1:
        if s == "B":
            print(count)
        else:
            print(n)
    else:
        pref = [0]*(n+1)
        for i in range(1, n+1):
            pref[i] = pref[i-1]
            if s[i-1] == "W":
                pref[i] += 1

        ans = 1000000
        for i in range(k, n+1):
            ans = min(ans, pref[i]-pref[i-k])

        print(ans)