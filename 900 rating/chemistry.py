t = int(input())


def result(string, n, k):
    if n == 1 or n-k == 1:
        return "YES"
    count = [0 for i in range(26)]
    for i in range(n):
        count[ord(string[i]) - ord("a")] ^= 1
    cnt = sum(count)
    if cnt - 1 > k:
        return "NO"
    return "YES"



while t>0:
    t-=1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    k = arr[1]
    s = input()
    print(result(s,n,k))
