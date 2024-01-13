n = int(input())


def sum_of_round(num):
    arr = []
    multiple = 1
    while num > 0:
        if num % 10 != 0:
            rem = int(num % 10)
            # print(f"rem = {rem}")
            rem = int(rem * multiple)
            arr.append(rem)
        num = int(num/10)
        multiple = int(multiple * 10)

    print(len(arr))
    print(" ".join([str(a) for a in arr]))


while n > 0:
    n -= 1
    a = int(input())
    sum_of_round(a)
