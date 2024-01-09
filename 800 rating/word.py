word = input()
lower_count = 0
upper_count = 0

for i in range(len(word)):
    if word[i] > word[i].upper():
        lower_count += 1

upper_count = len(word) - lower_count

if lower_count < upper_count:
    print(word.upper())
else:
    print(word.lower())