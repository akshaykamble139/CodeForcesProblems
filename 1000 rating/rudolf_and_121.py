t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(a) for a in input().split()]

    i = 1
    has_ans = True
    while has_ans and i < n - 1:
        # print(f"arr = {arr}")
        if arr[i - 1] == 0:
            i += 1
        else:
            if arr[i] == 0 or arr[i + 1] == 0:
                has_ans = False
                break
            else:
                g = min(arr[i - 1], arr[i + 1])
                h = (arr[i] - g) // 2
                if arr[i] == 2 * g:
                    k = g
                else:
                    k = min(g, h)
                if k == 0:
                    has_ans = False
                    break
                # print(f"k = {k} g = {g} h = {h}")
                arr[i - 1] -= k
                arr[i] -= 2 * k
                arr[i + 1] -= k
                # print(f"after arr = {arr}")
                if arr[i + 1] == 0 and arr[i-1] > 0:
                    has_ans = False
                    break
                elif arr[i-1] == arr[i] == arr[i+1] == 0:
                    i += 1

    if has_ans and arr[-3] == arr[-2] == arr[-1] == 0:
        print("YES")
    else:
        print("NO")
