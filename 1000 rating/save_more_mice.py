t = int(input())

while t > 0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    arr = [int(a) for a in input().split()]
    arr.sort()
    cat_position = 0
    mice = 0
    # print(arr)
    for i in range(k-1,-1,-1):
        # print(cat_position)
        if cat_position >= n or cat_position + n-arr[i] > arr[i]:
            if cat_position < arr[i]:
                mice+=1
            break
        else:
            # print(f"cat_position = {cat_position} i = {i} n = {n} arr[{i}] = {arr[i]}")
            cat_position += n-arr[i]
            mice += 1

    print(mice)


