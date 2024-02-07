n = int(input())

arr = [int(a) for a in input().split()]

f_high = 0
s_high = 0

f_low = 1000000
s_low = 1000000

for a in arr:
    if a>f_high:
        s_high = f_high
        f_high = a
    elif a>s_high:
        s_high = a
    if a<f_low:
        s_low = f_low
        f_low = a
    elif a<s_low:
        s_low = a

print(min(s_high-f_low, f_high-s_low))
