from math import ceil

t = int(input())

while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    x = word[1]
    arr = [int(a) for a in input().split()]
    low = ceil(sum(arr) / x)
    high = sum([ceil(a / x) for a in arr])

    print(f"{low} {high}")
