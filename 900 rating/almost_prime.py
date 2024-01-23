n = int(input())

from math import sqrt
if n<6:
    print(0)
else:

    def is_prime(num):
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


    count = 0
    primes = [2,3]
    for a in range(4,n+1):
        if is_prime(a):
            primes.append(a)

    for i in range(6, n+1):
        temp = len([a for a in primes if i % a == 0])
        if temp == 2:
            count += 1

    print(count)
