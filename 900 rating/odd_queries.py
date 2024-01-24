t = int(input())

while t>0:
    t-=1
    word = [int(a) for a in input().split()]
    n = word[0]
    q = word[1]
    arr = [int(a) for a in input().split()]
    pref = [0]
    curr = 0
    for i in range(len(arr)):
        curr += arr[i]
        pref.append(curr)

    # print(pref)

    while q > 0:
        q -=1
        temp = [int(a) for a in input().split()]
        l = temp[0]
        r = temp[1]
        k = temp[2]
        extra = (r-l+1)*k
        value = pref[n] - (pref[r] - pref[l-1]) + extra
        if value % 2 == 0:
            print("NO")
        else:
            print("YES")
