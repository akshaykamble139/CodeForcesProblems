t = int(input())


def result(arr:[]):
    if len(arr) == 1:
        return "YES"
    if len(arr) == 2:
        if abs(arr[0]-arr[1]) % 2 == 0:
            return "YES"
        else:
            return "NO"
    first = arr[0] % 2
    for a in arr:
        if a%2 != first:
            return "NO"
    return "YES"



while t>0:
    t-= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    print(result(arr))
