n = int(input())
arr = [int(a) for a in input().split()]
arr.sort()
arr = [str(a) for a in arr]
print(" ".join(arr))