string = input()
arr = string.split("+")
should_sort = False
start = int(arr[0])
for i in range(1,len(arr)):
    if int(arr[i]) >= start:
        start = int(arr[i])
    else:
        should_sort = True

if should_sort:
    arr.sort()
print("+".join(arr))