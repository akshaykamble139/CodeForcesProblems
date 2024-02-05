n = int(input())
arr = [int(a) for a in input().split()]

total = sum(arr)
odd = len([a for a in arr if a%2 == 1])
even = len([a for a in arr if a%2 == 0])

if total % 2 == 0:
    print(even)
else:
    print(odd)
