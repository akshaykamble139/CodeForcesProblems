word = [int(a) for a in input().split()]
n=word[0]
q=word[1]

arr=[int(a) for a in input().split()]
arr.sort()
prefix = [0]
total = 0
for i in range(n):
    total = prefix[i] + arr[i]
    prefix.append(total)
# print(arr)
# print(prefix)
while q>0:
    q-=1
    query = [int(a) for a in input().split()]
    x = query[0]
    y = query[1]
    curr = prefix[n-x+y] - prefix[n-x]
    print(curr)

