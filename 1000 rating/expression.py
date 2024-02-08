a = int(input())
b = int(input())
c = int(input())

high = a*b*c

if (a+b)*c > high:
    high = (a+b)*c
if a*(b+c) > high:
    high = a*(b+c)
if a+b*c > high:
    high = a+b*c
if a*b+c > high:
    high = a*b+c
if a+b+c > high:
    high = a+b+c

print(high)