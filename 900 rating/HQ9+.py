word = input()

count = 0

for a in word:
    if a == 'H' or a == "Q" or a == "9":
        count += 1
        break

if count > 0:
    print("YES")
else:
    print("NO")