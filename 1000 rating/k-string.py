k = int(input())
word = input()

dict = {}
for a in word:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1

has_answer = True
ans = ""
for key, v in dict.items():
    if v%k != 0:
        has_answer = False
        break
    else:
        ans += (key * (v//k))

if not has_answer:
    print(-1)
else:
    print(ans * k)