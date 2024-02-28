word = [int(a) for a in input().split()]

n = word[0]
m = word[1]

rooms = [int(a) for a in input().split()]

letters = [int(a) for a in input().split()]

i = 0
j = 0
curr = 0
total = [0]
for a in rooms:
    curr += a
    total.append(curr)

# print(total)
while i < len(total) and j < m:
    if total[i] >= letters[j]:
        print(i, letters[j]-total[i-1])
        j += 1
    else:
        i += 1
