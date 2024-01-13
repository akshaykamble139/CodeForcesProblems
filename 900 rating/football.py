word = input()

if word.find("0000000") != -1 or word.find("1111111") != -1:
    print("YES")
else:
    print("NO")