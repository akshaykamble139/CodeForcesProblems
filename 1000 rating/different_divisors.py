t = int(input())


def is_prime(n):
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i += 1
    return True


primes = []
for i in range(2, 50001):
    if is_prime(i):
        primes.append(i)

while t>0:
    t -= 1
    d = int(input())
    x = 0
    for i in primes:
        if i>d:
            x = i
            break

    y = 0
    for i in primes:
        if i>=x+d:
            y = i
            break

    print(x*y)
