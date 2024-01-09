n = int(input())

max = 0
curr = 0
for _ in range(n):
    word = input()
    arr = word.split()
    enter = int(arr[1])
    leave = int(arr[0])
    curr = curr + enter - leave
    if curr > max:
        max = curr

print(max)
