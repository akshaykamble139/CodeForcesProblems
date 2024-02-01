t = int(input())


def result(arr, n):
    if n == 1:
        return "NO"
    ones = len([a for a in arr if a == 1])
    total = sum(arr)

    if total < ones + n:
        return "NO"
    return "YES"


while t > 0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    print(result(arr,n))
