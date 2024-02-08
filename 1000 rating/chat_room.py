word = input()
n = len(word)
text = "hello"
index = 1
if n < 5:
    print("NO")
else:
    arr = [i for i in range(n) if word[i] == "h"]
    if len(arr) == 0:
        print("NO")
    else:
        has_answer = False
        for a in arr:
            if not has_answer:
                index = 1
                for i in range(a+1,n):
                    if word[i] == text[index]:
                        index += 1
                        if index == 5:
                            has_answer = True
                            break
            else:
                break

        if has_answer:
            print("YES")
        else:
            print("NO")




