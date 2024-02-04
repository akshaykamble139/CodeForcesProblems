word = [int(a) for a in input().split()]
n = word[0]
m = word[1]

arr = [int(a) for a in input().split()]

l_arr = [0]
for i in range(1,n):
    l_arr.append(max(0, arr[i] - arr[i-1]))

r_arr = [0]
for i in range(n-1):
    r_arr.append(max(0, arr[i] - arr[i+1]))

for i in range(n-1):
    l_arr[i+1] += l_arr[i]
    r_arr[i+1] += r_arr[i]

while m>0:
    m -= 1
    temp = [int(a) for a in input().split()]
    s = temp[0]
    t = temp[1]
    if s < t:
        print(r_arr[t-1] - r_arr[s-1])
    else:
        print(l_arr[s-1] - l_arr[t-1])



