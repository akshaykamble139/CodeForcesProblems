n = int(input())
value = 0
for _ in range(n):
    word = input().lower()
    if word[1] == '+':
        value += 1
    else:
        value -= 1

print(value)

