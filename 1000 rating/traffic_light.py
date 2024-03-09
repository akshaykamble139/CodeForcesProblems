t = int(input())

for _ in range(t):
    word = input().split()
    n = int(word[0])
    curr_color = word[1]
    pattern = input()
    total = pattern + pattern

    if curr_color == "g":
        print(0)
    else:
        arr = [0] * (2*n)
        for i in range(len(total)-1, -1, -1):
            if i == len(total)-1:
                if total[i] != "g":
                    arr[i] = -1
            else:
                if total[i] != "g":
                    if arr[i+1] == -1:
                        arr[i] = arr[i+1]
                    else:
                        arr[i] = arr[i+1] + 1

        print(max([arr[i] for i in range(n) if pattern[i] == curr_color]))
