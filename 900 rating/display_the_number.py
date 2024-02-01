t = int(input())

dict = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

while t > 0:
    t -= 1
    n = int(input())
    if n%2 == 1:
        if n == 3:
            print("7")
        else:
            print("7" + "1"*((n-3)//2))
    else:
        print("1"*(n//2))
