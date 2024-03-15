n = int(input())

arr = []
diagonal = ""
others = ""
has_x = True
for i in range(n):
    word = input()
    if i == 0:
        diagonal = word[0]
        others = word[1]
        if diagonal == others:
            has_x = False
            break
        g = diagonal + others*(n-2) + diagonal
        if g != word:
            # print("first row failure")
            has_x = False
            break
    elif i == n-1:
        g = diagonal + others*(n-2) + diagonal
        if g != word:
            # print("last row failure")
            has_x = False
            break
    else:
        mid = n//2
        if i > mid:
            i = mid-(i-mid)
        g = others*i + diagonal + others * (mid-i)
        if n % 2 == 1:
            if g + g[::-1][1:] != word:
                # print(f"i = {i} mid = {mid} odd square failure {g + g[::-1][1:]} == {word}")
                has_x = False
                break
        else:
            if g + g[::-1] != word:
                # print(f"i = {i} mid = {mid} even square failure {g + g[::-1]} == {word}")
                has_x = False
                break

if has_x:
    print("YES")
else:
    print("NO")
