word = [int(a) for a in input().split()]
n = word[0]
d = word[1]
arr = [int(a) for a in input().split()]
total = sum(arr)

if total + (n-1)*10 > d:
    print(-1)
else:
    count = (d - total)//5
    print(count)
