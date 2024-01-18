shift_direction = input()
word = input()

arr = [
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./",
]

shift = 1 if shift_direction == "L" else -1

result = ""

for a in word:
    for c in arr:
        if a in c:
            result += c[c.find(a) + shift]
            break

print(result)