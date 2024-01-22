arr = []
for _ in range(3):
    word = [int(a) for a in input().split()]
    arr.append(word)

switched = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        curr = arr[i][j]
        switched[i][j] += curr
        if i - 1 >= 0:
            switched[i - 1][j] += curr
        if j - 1 >= 0:
            switched[i][j - 1] += curr
        if i + 1 < 3:
            switched[i + 1][j] += curr
        if j + 1 < 3:
            switched[i][j + 1] += curr

for i in range(3):
    a = abs(1-switched[i][0]%2)
    b = abs(1-switched[i][1]%2)
    c = abs(1-switched[i][2]%2)
    print(f"{a}{b}{c}")
