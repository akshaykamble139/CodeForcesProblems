arr = [int(a) for a in input().split()]

l = []
for a in arr:
    if a not in l:
        l.append(a)

print(len(arr)-len(l))
