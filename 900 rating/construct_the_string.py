import random
t = int(input())

arr = [a for a in "abcdefghijklmnopqrstuvwxyz"]


def result(n, a, b):
    char_choice = arr
    word = ""
    substring = ""
    distinct_substring = 0
    for i in range(n):
        # print(f"word = {word} substring = {substring}")
        if word == "":
            word += char_choice[0]
            substring += word
            distinct_substring += 1
        else:
            if len(substring) == b:
                substring = substring[1:]
                distinct_substring -= 1

            c = [a for a in char_choice if a not in substring][0]
            word += c
            substring += c
            distinct_substring += 1

    print(word)



while t>0:
    t-=1
    word = [int(a) for a in input().split()]
    n = word[0]
    a = word[1]
    b = word[2]
    result(n,a,b)

