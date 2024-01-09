n = int(input())
word = input().split()
arr = [int(a) for a in word]

sum = 0
for a in arr:
    sum += a

print(100*(sum/(n*100)))