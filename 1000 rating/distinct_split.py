t = int(input())

while t>0:
    t -= 1
    n = int(input())
    word = input()

    s = set()
    p = [0]*n
    for i in range(n):
        s.add(word[i])
        p[i] = len(s)

    ans = 0
    s.clear()
    # print(p)
    for i in range(n-1,0,-1):
        s.add(word[i])
        ans = max(ans, len(s) + p[i-1])
        # print(f"ans = {ans}")

    print(ans)
