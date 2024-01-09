k_n_w = input()
arr = k_n_w.split()
k = int(arr[0])
n = int(arr[1])
w = int(arr[2])

cost = 0
for i in range(w):
    cost += (i+1)*k

if cost > n:
    print(cost - n)
else:
    print(0)