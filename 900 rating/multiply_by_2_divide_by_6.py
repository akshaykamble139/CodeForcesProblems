t = int(input())


def get_result(num):
    if num == 1:
        return 0
    if num == 2 or num % 3 != 0:
        return -1
    count = 0
    while num % 3 == 0:
        if num % 2 == 0:
            num /= 6
            count += 1
        else:
            num *= 2
            num /= 6
            count += 2

    if num == 1:
        return count
    return -1


while t > 0:
    t -= 1
    n = int(input())
    print(get_result(n))
