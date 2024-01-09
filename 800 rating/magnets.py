n = int(input())
count = 1
prev = input()
n -= 1
while n>0:
    word = input()
    if word != prev:
        count += 1
    n -= 1
    prev = word

print(count)
