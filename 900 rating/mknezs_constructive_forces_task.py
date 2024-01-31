t = int(input())

while t>0:
    t-=1
    n=int(input())
    if n == 1 or n == 3:
        print("NO")
    elif n%2 == 1:
        print("YES")
        ans = ""
        mid = n//2
        first = n//2-1
        for i in range(n):
            if i%2 == 1:
                ans += str(mid*-1) + " "
            else:
                ans += str(first) + " "
        print(ans)
    else:
        print("YES")
        ans = ""
        num = 1
        for i in range(n):
            ans += str(num) + " "
            num *= -1
        print(ans)
