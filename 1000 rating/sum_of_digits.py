n = input()
count = 0
while len(n) > 1:
    s = 0
    for a in n:
        s += int(a)
    n = str(s)
    count += 1

print(count)