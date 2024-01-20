t = int(input())


def result(num):
    if num < 10:
        return num
    val = ""
    curr = 9
    while num > 0 and curr > 0:
        num -= curr
        val += str(curr)
        curr -= 1
        if num < 10 and str(num) not in val:
            val += str(num)
            curr = 0
            num = 0

        # print(f"val = {val} num = {num}")

    if num == 0:
        return int(val[::-1])
    return -1


while t>0:
    t -= 1
    n = int(input())
    print(result(n))
