n = int(input())
sum = 0
for _ in range(n):
    curr_sum = 0
    l = input()
    arr = l.split()
    for a in arr:
        curr_sum += int(a)
    if curr_sum > 1:
        sum += 1

print(sum)