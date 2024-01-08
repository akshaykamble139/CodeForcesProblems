n = int(input())
for _ in range(n):
    word = input()
    length = len(word)
    if length > 10:
        word = word[0] + str(length-2) + word[-1]
    print(word)
