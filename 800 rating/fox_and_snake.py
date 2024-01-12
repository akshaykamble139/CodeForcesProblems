word = [int(a) for a in input().split()]
n = word[0]
m = word[1]

for i in range(1, n+1):
    if i % 2 == 1:
        print("#"*m)
    elif i % 4 == 0:
        print("#" + "."*(m-1))
    elif i % 2 == 0:
        print("."*(m-1) + "#")
