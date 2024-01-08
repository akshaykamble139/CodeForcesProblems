arr = []
i = 0
j = 0
for index in range(5):
    row_str = input()
    if '1' in row_str:
        arr = row_str.split()
        j = arr.index('1',0)
        i = index

print(abs(i - 2) + abs(j - 2))
