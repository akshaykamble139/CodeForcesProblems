n = int(input())

arr = [
    4, 7,
    44, 77, 47, 74,
    444, 777, 477, 747, 774, 447, 474, 744
]

is_div = False
for a in arr:
    if n%a == 0:
        is_div = True
        break

if is_div:
    print("YES")
else:
    print("NO")