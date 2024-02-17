n = int(input())
num = 0
arr = []
for i in range(n+1):
    blank = "  "*(n - i)
    if i == 0:
        print(blank + "0")
        arr.append(blank + "0")
    else:
        s = ""
        for j in range(i):
            s += str(j)
        s = s + str(i) + s[::-1]
        g = blank + " ".join([a for a in s])
        print(g)
        arr.append(g)

for a in arr[:n][::-1]:
    print(a)