arr = [int(a) for a in input().split()]
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]

m = max(3*a/10, a - ((a/250)*c))
v = max(3*b/10, b - ((b/250)*d))

if m<v:
    print("Vasya")
elif m>v:
    print("Misha")
else:
    print("Tie")