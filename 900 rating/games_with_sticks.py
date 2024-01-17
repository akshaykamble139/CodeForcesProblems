arr = [int(a) for a in input().split()]

n = arr[0]
m = arr[1]
product = n * m
akshat_chance = True

while n > 0 and m > 0:
    product -= (m + n - 1)
    m -= 1
    n -= 1
    akshat_chance = not akshat_chance

if not akshat_chance:
    print("Akshat")
else:
    print("Malvika")