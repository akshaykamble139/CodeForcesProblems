t = int(input())


def result(x, n):
    if n == 0:
        return x
    ans = 0
    if n%4 == 1:
        ans = -n
    elif n%4 == 2:
        ans = 1
    elif n%4 == 3:
        ans = n+1

    if x%2 == 0:
        return ans + x
    else:
        return x - ans


while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    initial = word[0]
    jumps = word[1]

    print(result(initial,jumps))
