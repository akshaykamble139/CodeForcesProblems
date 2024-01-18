n = int(input())
word = input()

ones = word.count("1")
zeroes = word.count("0")

print(abs(ones-zeroes))
