n_and_t = input()
arr = n_and_t.split()
n = int(arr[0])
t = int(arr[1])

word = input()


def rearrange(queue):
    first = 0
    i = 1
    ans = ""
    while i < len(queue):
        # print(f"ans = {ans} first = {first} i = {i}")
        if queue[i] == 'G' and queue[first] == 'B':
            ans += "GB"
            first = i+1
            i = first+1
        else:
            ans += queue[first]
            first = i
            i += 1

    if len(ans) < len(queue):
        ans += queue[-1]
    # print(f"last ans = {ans} first = {first} i = {i}")
    return ans


for _ in range(t):
    word = rearrange(word)

print(word)
