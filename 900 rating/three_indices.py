t = int(input())

while t>0:
    t -= 1
    n = int(input())
    arr = [int(a) for a in input().split()]
    answer_found = False
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            print("YES")
            print(f"{i} {i+1} {i+2}")
            answer_found = True
            break

    if not answer_found:
        print("NO")

