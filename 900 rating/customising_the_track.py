t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    total = sum(arr)
    k = total%n
    ans = k*(n-k)
    print(ans)



