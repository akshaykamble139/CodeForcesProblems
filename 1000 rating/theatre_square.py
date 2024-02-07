arr = [int(a) for a in input().split()]
n = arr[0]
m = arr[1]
a = arr[2]

l = n//a
if n%a != 0:
    l += 1
r = m//a
if m%a != 0:
    r += 1

print(l*r)