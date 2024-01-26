t = int(input())

while t>0:
    t-=1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    arr = [int(a) for a in input().split()]
    estimate = []
    for i in range(n):
        estimate.append((arr[i],i))

    actual = [int(a) for a in input().split()]
    estimate.sort()
    actual.sort()
    ans = ["" for i in range(n)]
    for i in range(n):
        ans[estimate[i][1]] = str(actual[i])
    print(" ".join(ans))
