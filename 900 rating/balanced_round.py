t = int(input())


def result():
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    arr = [int(a) for a in input().split()]
    arr.sort()
    count = 1
    answer = 1

    # print(arr)

    for i in range(1,n):
        if arr[i] - arr[i-1] > k:
            count = 1
        else:
            count += 1
        # print(f"count = {count} arr[{i}] = {arr[i]} arr[{i-1}] = {arr[i-1]}")
        answer = max(answer,count)

    print(n - answer)


while t > 0:
    t -= 1
    result()
