n = int(input())
arr = [int(a) for a in input().split()]
least = min(arr)
if arr.count(least) > 1:
    print("Still Rozdil")
else:
    print(arr.index(least)+1)