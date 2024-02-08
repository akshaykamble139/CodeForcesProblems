n = int(input())

x = 0
y = 0
z = 0
while n>0:
    n -= 1
    word = [int(a) for a in input().split()]
    x += word[0]
    y += word[1]
    z += word[2]

if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
