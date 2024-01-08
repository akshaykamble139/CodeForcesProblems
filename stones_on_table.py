n = int(input())
word = input()
count = 0
first = word[0]

for i in range(1, len(word)):
    if first == word[i]:
        count += 1
    else:
        first = word[i]

print(count)
