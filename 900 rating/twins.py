n = int(input())

arr = [int(a) for a in input().split()]
arr.sort()
total = sum(arr)
count = 1
curr_sum = arr[-1]
if curr_sum > total - curr_sum:
    print(count)
else:
    for i in range(n-1)[::-1]:
        count += 1
        curr_sum += arr[i]
        if curr_sum > total - curr_sum:
            print(count)
            break
