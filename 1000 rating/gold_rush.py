t = int(input())

dict = {}


def check(a, b):
    if a == b:
        return True
    if a%3 != 0:
        return False
    if (a,b) in dict:
        return dict[(a,b)]

    ans = check(a//3,b) or check(2*a//3, b)
    dict[(a,b)] = ans
    return ans


while t>0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    m = word[1]
    helper = [n]
    if check(n, m):
        print("YES")
    else:
        print("NO")
