t = int(input())

from math import floor


def result(num):
    if num < 1:
        return 0
    if num < 10:
        return num

    mul = floor(num/9)
    count = 0
    if num % 9 == 0:
        count = 9 + (mul-1) * 10
    else:
        count = num % 9 + mul * 10


    return count


while t>0:
    t -= 1
    n = int(input())
    print(result(n))