word = input()
arr = []
for i in range(len(word)):
    if word[i] not in arr:
        arr.append(word[i])

if len(arr) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

