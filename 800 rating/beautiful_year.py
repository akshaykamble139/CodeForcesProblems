n = int(input())


def is_distinct(num):
    arr = []
    for i in range(len(num)):
        if num[i] not in arr:
            arr.append(num[i])

    return len(num) == len(arr)


n += 1
while not is_distinct(str(n)):
    n += 1

print(n)