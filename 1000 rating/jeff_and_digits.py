n = int(input())
arr = [int(a) for a in input().split()]

fives = len([a for a in arr if a == 5])
zeroes = len(arr) - fives

if fives >= 9 and zeroes > 0:
    fives -= fives%9
    print("5"*fives + "0"*zeroes)
else:
    if zeroes == 0:
        print(-1)
    else:
        print(0)