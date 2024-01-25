t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    k = arr[1]
    x = arr[2]
    low = int(k*(k+1)/2)
    high = int((n*(n+1)/2) - (n-k)*(n-k+1)/2)
    if low<=x<=high:
        print("YES")
    else:
        print("NO")