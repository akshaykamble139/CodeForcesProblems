t = int(input())

while t>0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    k = word[1]
    arr = [int(a) for a in input().split()]

    start = 1
    for i in range(n):
        if arr[i] == start:
            start+=1

    # print(f"start = {start}")

    # if start == n+1:
    #     print(0)
    # else:
    ans = (n-start+k)//k
    print(ans)