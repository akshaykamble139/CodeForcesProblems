t = int(input())

while t>0:
    t -= 1
    word = [int(a) for a in input().split()]
    n = word[0]
    H = word[1]
    M = word[2]
    sleep_time = H*60 + M
    h_diff = 24
    m_diff = 60
    diff_min = 24*60
    for _ in range(n):
        arr = [int(a) for a in input().split()]
        h = arr[0]
        m = arr[1]
        curr_time = h*60 + m
        if curr_time < sleep_time:
            curr_time += (24*60)
        diff = curr_time - sleep_time
        if diff_min > diff :
            diff_min = diff

    hour = diff_min // 60
    minutes = diff_min % 60
    print(f"{hour} {minutes}")






