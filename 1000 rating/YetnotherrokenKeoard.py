t = int(input())

for _ in range(t):
    word = input()
    s = [c for c in word]
    n = len(s)
    upper = []
    lower = []
    for i in range(n):
        if s[i] == 'b':
            s[i] = ''
            if lower:
                s[lower.pop()] = ''
            continue
        if s[i] == 'B':
            s[i] = ''
            if upper:
                s[upper.pop()] = ''
            continue
        if 'a' <= s[i] <= 'z':
            lower += [i]
        else:
            upper += [i]
    print(''.join(s))

