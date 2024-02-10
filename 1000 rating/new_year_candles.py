word = [int(a) for a in input().split()]

a = word[0]
b = word[1]

ans = 0
rem = a
leftovers = 0

while rem > 0:
    ans += rem
    leftovers += rem
    rem = leftovers//b
    leftovers -= rem*b

print(ans)