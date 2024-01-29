t = int(input())


def result(arr,n):
    ans = 0
    for i in range(n - 1)[::-1]:
        while arr[i] >= arr[i + 1] and arr[i] > 0:
            arr[i] //= 2
            ans += 1

        if arr[i] == arr[i + 1]:
            return -1
    return ans


while t>0:
    t-=1
    n = int(input())
    arr = [int(a) for a in input().split()]
    print(result(arr,n))
