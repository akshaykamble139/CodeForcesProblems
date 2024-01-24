t = int(input())

answers = {}


def f(num):
    global answers
    if num in answers:
        return answers[num]
    if num % 2 == 0:
        answers[num] = 2
        return 2
    for i in range(3,num+1,2):
        if num%i == 0:
            answers[num] = i
            return i
    answers[num] = num
    return num


while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    k = arr[1]
    result = 0
    if n%2 == 0:
        result = n + k*2
    else:
        result = n + (k-1)*2 + f(n)
    print(result)

