t = int(input())

while t>0:
    t -= 1
    arr = [int(a) for a in input().split()]
    n = arr[0]
    m = arr[1]
    x = arr[2]
    y = arr[3]
    y = min(y, 2*x)
    ans = 0
    for _ in range(n):
        word = input()
        i = 0
        while i<m:
            if word[i] == "*":
                i += 1
            else:
                j = i
                while j + 1 < m and word[j+1] == ".":
                    j += 1
                seg = j-i+1
                ans += (seg%2) * x + (seg//2) * y
                i = j+1
    print(ans)
