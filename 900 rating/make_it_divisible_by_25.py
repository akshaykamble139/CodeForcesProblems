t = int(input())

def result(a, b):
    l = len(a)-1
    ans = 0
    while l >= 0 and a[l] != b[1]:
        l -= 1
        ans += 1

    if l<0:
        return 100
    l -= 1
    while l>=0 and a[l] != b[0]:
        l -= 1
        ans += 1

    if l<0:
        return 100
    return ans


while t>0:
    t -= 1
    n = input()
    if int(n)%25 == 0:
        print(0)
    else:
        arr = ["00", "25", "50", "75"]
        ans = 100
        for a in arr:
            ans = min(ans, result(n,a))

        print(ans)
