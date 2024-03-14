q = int(input())

for _ in range(q):
    s = input()
    t = input()

    if t.count("a") > 0:
        if len(t) == 1:
            print(1)
        else:
            print(-1)
    else:
        n = len(s)
        print(2**n)
