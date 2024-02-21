n = int(input())

start = -1
end = -1
count = 0

timings = []
for _ in range(n):
    arr = [int(a) for a in input().split()]
    timings.append(arr[0]*60 + arr[1])

prev_timing = timings[0]
max_cash = 1
curr_cash = 1

for a in timings[1:]:
    if a == prev_timing:
        curr_cash += 1
        if curr_cash > max_cash:
            max_cash = curr_cash
    else:
        curr_cash = 1
        prev_timing = a

print(max_cash)



