n = int(input())

arr = [int(a) for a in input().split()]

arr.sort()

has_answer = False
for i in range(1,n-1):
    if arr[i-1] + arr[i] > arr[i+1]:
        print("YES")
        has_answer = True
        break

if not has_answer:
    print("NO")
