t = int(input())


def result(num):
    val = max(6,num)
    intermediate = (val+1)//2
    return intermediate * 5


while t > 0:
    t -= 1
    n = int(input())
    print(result(n))
