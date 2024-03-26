t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(8)
    else:
        f = (n + 3) // 4
        print("9" * (n - f) + "8" * (f))
