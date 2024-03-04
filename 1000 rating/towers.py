n = int(input())

arr = [int(a) for a in input().split()]

dict = {}
high = 1
for a in arr:
    if a in dict:
        dict[a] += 1
        if high < dict[a]:
            high = dict[a]
    else:
        dict[a] = 1

k = len(dict)
print(high, k)