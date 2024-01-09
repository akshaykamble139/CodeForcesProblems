m_and_n = input()
arr = m_and_n.split()
m = int(arr[0])
n = int(arr[-1])

ans = 0
if m == 1 and n == 1:
    ans = 0
elif m == 1 or n == 1:
    if m == 1:
        ans = n/2
    else:
        ans = m/2
elif m % 2 == 0 or n % 2 == 0:
    ans = m * n / 2
else:
    ans = ((m-1) * (n-1) / 2) + (m-1)/2 + (n-1)/2

print(int(ans))