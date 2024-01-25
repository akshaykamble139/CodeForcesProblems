n = int(input())

arr = [int(a) for a in input().split()]
if n < 3:
    print(0)
else:
    low = min(arr)
    high = max(arr)
    word = [a for a in arr if low<a<high]
    print(len(word))