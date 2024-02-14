import math
q = int(input())


def result(a,b):
    l1 = len(a)
    l2 = len(b)
    g = math.gcd(l1,l2)

    if a *(l2//g) == b *(l1//g):
        return a*(l2//g)
    return -1


while q>0:
    q -= 1
    s = input()
    t = input()

    print(result(s,t))


