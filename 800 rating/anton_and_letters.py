word = input().lower()
word = word.replace("{","")
word = word.replace("}","")
arr = word.split(", ")
distinct = []
for a in arr:
    if a not in distinct and 'a' <= a <= 'z':
        distinct.append(a)

print(len(distinct))
