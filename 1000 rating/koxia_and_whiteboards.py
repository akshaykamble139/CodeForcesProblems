t = int(input())

for _ in range(t):
    word = [int(a) for a in input().split()]
    n = word[0]
    m = word[1]
    arr = [int(a) for a in input().split()]
    new = [int(a) for a in input().split()]

    for i in range(m):
        arr[arr.index(min(arr))] = new[i]

    print(sum(arr))

