a = input()
b = input()

arr = []
for i in range(len(a)):
    if a[i] != b[i]:
        arr.append('1')
    else:
        arr.append('0')

print("".join(arr))
