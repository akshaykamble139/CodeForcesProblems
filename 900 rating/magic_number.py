n = input()

if "444" in n:
    print("NO")
else:
    n = n.replace("144","")
    n = n.replace("14","")
    n = n.replace("1","")

    if n == "":
        print("YES")
    else:
        print("NO")