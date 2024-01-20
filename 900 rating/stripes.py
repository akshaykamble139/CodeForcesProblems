t = int(input())

all_red = "R"*8
all_blue = "B"*8


def result():
    arr = []
    r = []
    for i in range(8):
        word = input()
        arr.append(word)
        for a in word:
            if a == "R":
                r.append(i)

    for i in r:
        ok = True
        for j in range(8):
            if arr[i][j] != "R":
                ok = False
                break

        if ok:
            print("R")
            return

    print("B")
    return


while t>0:
    t -= 1
    input()
    result()
