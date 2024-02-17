n = int(input())

arr = [int(a) for a in input().split()]
i = 0
total = 0
has_answer = False
while not has_answer:
    total += arr[i % 7]
    i += 1
    if total >= n:
        if i%7 == 0:
            print(7)
        else:
            print(i%7)
        has_answer = True
