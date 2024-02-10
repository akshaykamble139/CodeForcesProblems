t = int(input())

while t>0:
    t -= 1
    n = int(input())
    word = input()

    f = ""
    for a in word:
        if a == "(":
            f += a
        else:
            if len(f) > 0 and f[len(f)-1] == "(":
                f = f[:-1]
            else:
                f += a
    print(len(f)//2)