a = input()
b = input()

if a == b:
    print(0)
else:
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 and j >= 0 and a[i] == b[j]:
        i -= 1
        j -= 1

    print(i + j + 2)
