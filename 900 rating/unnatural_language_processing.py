t = int(input())

V = ["a", "e"]
C = ["b", "c", "d"]
while t>0:
    t -= 1
    n = int(input())
    word = input().lower()
    first = word[0]
    second = word[1]
    ans = ""
    i = 2
    completed = False
    while i<n:
        # print(f"ans = {ans} i  = {i} letter = {word[i]} first = {first} second = {second}")
        if (first in C and second in V) and word[i] in C:
            if i+2 < n:
                if word[i+1] in C:
                    ans += first + second + word[i] + "."
                    first = word[i+1]
                    second = word[i+2]
                    i += 3
                else:
                    ans += first + second + "."
                    first = word[i]
                    second = word[i+1]
                    i += 2
            else:
                if i == n-1:
                    ans += first + second + word[i]
                    completed = True
                elif i == n-2:
                    ans += first + second + "."
                    first = word[i]
                    second = word[i+1]
                break
    if not completed:
        ans += first + second
    print(ans)



