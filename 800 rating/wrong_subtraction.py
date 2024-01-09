n_and_k = input()
arr = n_and_k.split()
n = int(arr[0])
k = int(arr[1])

while k > 0:
    if n % 10 != 0:
        n -= 1
    else:
        n /= 10
    k -= 1

print(int(n))