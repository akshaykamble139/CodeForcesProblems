n = int(input())
word = input()
anton = 0
danik = 0
for i in range(n):
    if word[i] == "A":
        anton += 1
    else:
        danik += 1

if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print("Friendship")
