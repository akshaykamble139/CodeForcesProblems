n = input()
if n[0] == "-":
    common = n[:-2]
    if int(common + n[-1]) > int(n[:-1]):
        print(int(common + n[-1]))
    else:
        print(int(n[:-1]))

else:
    print(n)