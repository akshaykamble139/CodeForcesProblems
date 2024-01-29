n = int(input())

arr = [int(a) for a in input().split()]

ans = [arr[0]]
max_till_now = arr[0]
x = [0, max_till_now]
for i in range(1,n):
    a_i = arr[i] + max_till_now
    if max_till_now < a_i:
        max_till_now = a_i
    ans.append(a_i)

print(" ".join([str(j) for j in ans]))