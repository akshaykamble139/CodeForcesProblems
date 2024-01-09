n = int(input())

count = 0

for _ in range(n):
    word = input()
    arr = word.split()
    staying = int(arr[0])
    space = int(arr[1])
    if space - staying > 1:
        count += 1

print(count)