q = int(input())


def result(a, b, c):
    if a == b == c:
        return "YES"
    if 2*b == a+c:
        return "YES"
    # check if a can be modified
    diff1 = c-b
    if (b-diff1) > 0 and (b-diff1) % a == 0:
        return "YES"

    # check if b can be modified
    diff2 = c-a
    if (c-diff2) > 0 and diff2 % 2 == 0 and (c-(diff2/2)) % b == 0:
        return "YES"

    # check if c can be modified
    diff3 = b-a
    if (b+diff3) > 0 and (b+diff3) % c == 0:
        return "YES"

    return "NO"


while q > 0:
    q -= 1
    arr = [int(a) for a in input().split()]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    print(result(a, b, c))
