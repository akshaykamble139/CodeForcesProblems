word = [int(a) for a in input().split()]

n = word[0]
t = word[1]

arr = [int(a) for a in input().split()]

dict = {1}
i=1
while i<n:
    dict.add(i+arr[i-1])
    i = i+arr[i-1]

# print(dict)
if t in dict:
    print("YES")
else:
    print("NO")
