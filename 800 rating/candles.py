n = int(input())


def get_count(num):
    if num < 3:
        return 0
    if num % 2 == 1:
        return (num-1) // 2
    else:
        return (num-2) // 2


while n > 0:
    n -= 1
    t = int(input())
    print(get_count(t))