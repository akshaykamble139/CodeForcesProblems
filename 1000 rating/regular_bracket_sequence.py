t = int(input())

while t>0:
    t -= 1
    s = input()
    if len(s)%2 == 1:
        print("NO")
    elif s[0] != ")" and s[-1] != "(":
        print("YES")
    else:
        print("NO")