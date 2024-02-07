word = input().lower()

vowels = "aoyeui"
ans = ""

for a in word:
    if a not in vowels:
        ans += "." + a

print(ans)
