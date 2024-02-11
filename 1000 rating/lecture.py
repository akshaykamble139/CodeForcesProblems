word = [int(a) for a in input().split()]
n = word[0]
m = word[1]

dict = {}
for _ in range(m):
    arr = input().split()
    if len(arr[0]) <= len(arr[1]):
        dict[arr[0]] = arr[0]
    else:
        dict[arr[0]] = arr[1]

sentence = input().split()
ans = ""
for a in sentence:
    ans += dict[a] + " "

print(ans)