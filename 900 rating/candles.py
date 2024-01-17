t = int(input())

arr = []

for i in range(2,30):
    arr.append((2 ** i) - 1)



while t > 0:
    t -= 1
    n = int(input())
    # x * ((2^k)-1) = n
    modified_arr = [a for a in arr if a <= n and n % a == 0]
    print(n//modified_arr[-1])