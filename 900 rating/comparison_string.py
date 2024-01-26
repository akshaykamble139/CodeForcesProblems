t = int(input())

while t>0:
    t -= 1
    n = int(input())
    word = input()
    ans = 1
    curr = 1
    for i in range(1,n):
        if word[i]!=word[i-1]:
            curr = 1
        else:
            curr+=1
        ans = max(ans,curr)

    print(ans+1)
