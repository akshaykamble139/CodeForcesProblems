t = int(input())

while t>0:
    t -= 1

    word = [int(a) for a in input().split()]
    n=word[0]
    m=word[1]
    i=word[2]
    j=word[3]
    print(f"1 1 {n} {m}")
