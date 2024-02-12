arr = [int(a) for a in input().split()]

n = arr[0]
a = arr[1]
b = arr[2]

# 1 2 3 4 5
if n-b <= a:
    print(n-a)
else:
    print(b+1)
