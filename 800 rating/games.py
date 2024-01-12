n = int(input())

count = 0
total = n
away = []
home = []
# arr = []
while total > 0:
    total -= 1
    word = [int(a) for a in input().split()]
    # arr.append(word)
    home.append(word[0])
    away.append(word[1])
    # if word[1] in away:
    #     away[word[1]] = away[word[1]] + 1
    # else:
    #     away[word[1]] = 1
    #
    # if word[0] in home:
    #     home[word[0]] = home[word[0]] + 1
    # else:
    #     home[word[0]] = 1

for a in home:
    h = [b for b in away if a == b]
    count += len(h)

# print(home)
# print(away)
# for a in home:
#     if a in away:
#         print(f"common {a} home[{a}] = {home[a]} away[{a}] = {away[a]}")
#         count += max(home[a],away[a])

print(count)

