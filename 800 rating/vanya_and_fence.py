n_and_h = input()
arr = n_and_h.split()
n = int(arr[0])
h = int(arr[1])

count = 0
word = input()
heights = word.split()
for i in range(n):
    if int(heights[i]) > h:
        count += 2
    else:
        count += 1

print(count)
