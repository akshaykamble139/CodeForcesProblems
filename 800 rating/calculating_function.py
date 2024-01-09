n = int(input())


def calculate(num):
    product = -1
    if num % 2 == 0:
        return int(num/2)
    else:
        return int(((num + 1) * -1) / 2)


print(calculate(n))
