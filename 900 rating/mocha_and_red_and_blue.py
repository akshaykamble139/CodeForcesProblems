t = int(input())

while t>0:
    t -= 1
    n = int(input())
    word = input()
    blank = word.count("?")
    if blank == 0:
        print(word)
    elif blank == n:
        print(("BR"*((n+1)//2))[:n])
    else:
        ans = [a for a in word]
        for i in range(1,n):
            if ans[i] == "?" and ans[i-1] != "?":
                if ans[i-1] == "R":
                    ans[i] = "B"
                else:
                    ans[i] = "R"

        for i in range(0,n-1)[::-1]:
            if ans[i] == "?" and ans[i+1] != "?":
                if ans[i+1] == "R":
                    ans[i] = "B"
                else:
                    ans[i] = "R"

        print("".join(ans))
