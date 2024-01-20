t = int(input())

while t > 0:
    t -= 1
    word = input()
    ones = word.count("1")
    zeroes = word.count("0")
    if ones == 0 or zeroes == 0:
        print("NET")
    else:
        val = min(ones, zeroes)
        if val % 2 == 1:
            print("DA")
        else:
            print("NET")
