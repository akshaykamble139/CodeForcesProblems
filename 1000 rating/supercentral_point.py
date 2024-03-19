n = int(input())

X_arr = []
Y_arr = []

for _ in range(n):
    x,y = [int(a) for a in input().split()]
    X_arr.append([x,y])
    Y_arr.append([y,x])

X_arr.sort()
Y_arr.sort()

ans = 0

# print(X_arr)
# print(Y_arr)
prev = X_arr[0]
check = []
for i in range(1,n-1):
    [x,y] = X_arr[i]
    if X_arr[i-1][0] == X_arr[i][0] == X_arr[i+1][0]:
        check.append(X_arr[i])

for i in range(1,n-1):
    [y,x] = Y_arr[i]
    if Y_arr[i-1][0] == Y_arr[i][0] == Y_arr[i+1][0] and [x,y] in check:
        ans += 1

print(ans)