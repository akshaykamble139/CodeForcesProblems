n = int(input())
word = input().lower()
arr = []
for i in range(n):
    if word[i] not in arr:
        arr.append(word[i])

if len(arr) == 26:
    print("YES")
else:
    print("NO")
