t = int(input())


def solve(num, array):
    for i in range(num-1, -1, -1):
        if array[i] <= i+1:
            return i+2

    return 1


while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    arr.sort()
    print(solve(num=n, array=arr))
