n = int(input())

num = n
count = 0
while num > 0:
    if num >= 100:
        count += int(num/100)
        num = num - (100 * int(num/100))
    if num >= 20:
        count += int(num/20)
        num = num - (20 * int(num/20))
    if num >= 10:
        count += int(num/10)
        num = num - (10 * int(num/10))
    if num >= 5:
        count += int(num/5)
        num = num - (5 * int(num/5))
    if num >= 1:
        count += num
        num = num - num/1

print(count)
