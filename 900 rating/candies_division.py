t = int(input())

while t > 0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    k = arr[1]

    ans = n - (n%k)
    ans += min(n%k,k//2)
    print(ans)