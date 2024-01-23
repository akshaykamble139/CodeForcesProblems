t = int(input())


def result(a,k):
    if k==0:
        if a%2 == 0:
            return 0
        else:
            return 1
    if k == a:
        return 0
    elif k < a:
        diff = a - k
        return diff % 2
    else:
        diff = k - a
        return diff


while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    k = arr[1]
    print(result(n,k))