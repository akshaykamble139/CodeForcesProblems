t = int(input())

while t>0:
    t -= 1
    n = int(input())
    print(f"{(n+1)//2}")
    i = 1
    j = 3*n
    while i<j:
        print(f"{i} {j}")
        i += 3
        j -= 3
