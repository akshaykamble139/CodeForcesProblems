n = int(input())

if n<6:
    print(0)
elif n%2 == 1:
    print(0)
else:
    if n%4 == 0:
        print(n//4 - 1)
    else:
        print(n//4)