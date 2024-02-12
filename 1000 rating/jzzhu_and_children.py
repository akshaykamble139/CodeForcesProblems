word = [int(a) for a in input().split()]
n = word[0]
m = word[1]
arr = [int(a) for a in input().split()]

wait = [(a+m-1)//m for a in arr][::-1]
m = max(wait)
if m == 1:
    print(n)
else:
    print(n-wait.index(m))
