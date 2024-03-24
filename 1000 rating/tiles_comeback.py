t = int(input())

for _ in range(t):
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    arr = [int(a) for a in input().split()]

    d = {}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]].append(i)
        else:
            d[arr[i]] = [i]

    if len(d[arr[0]]) >= k and len(d[arr[-1]]) >=k:
        if arr[0] == arr[-1]:
            print("YES")
        elif d[arr[0]][k-1] < d[arr[-1]][-k]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

