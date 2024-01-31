n = int(input())

arr=[int(a) for a in input().split()]

evens = len([a for a in arr if a % 2 == 0])

if evens > n-evens:
    print(n-evens)
else:
    print(evens)
