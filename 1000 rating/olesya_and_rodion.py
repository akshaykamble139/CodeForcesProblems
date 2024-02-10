word = [int(a) for a in input().split()]

n = word[0]
t = word[1]

if n == 1 and t<10:
    print(t)
elif n == 1 and t==10:
    print(-1)
elif t == 10:
    print("1"+"0"*(n-1))
elif t in [2, 3, 4, 5, 6, 7, 8, 9]:
    print(str(t)*n)



