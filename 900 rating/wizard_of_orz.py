t = int(input())

while t>0:
    t -= 1
    n = int(input())
    if n<=3:
        print("989"[:n])
    else:
        s = "989"
        for i in range(3,n):
            s += str((i-3)%10)

        print(s)