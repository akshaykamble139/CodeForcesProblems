t = int(input())


def result(a,b,c,d):
    time_spent = b
    if time_spent >= a:
        return b
    if c <= d:
        return -1
    remaining_time_to_sleep = a-b
    sleep_per_alarm = c-d
    if remaining_time_to_sleep <= sleep_per_alarm:
        return b+c
    alarm_times = remaining_time_to_sleep//sleep_per_alarm
    if alarm_times*sleep_per_alarm == remaining_time_to_sleep:
        return b + alarm_times*c
    return b + (alarm_times+1)*c


while t>0:
    t -= 1
    arr = [int(z) for z in input().split()]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]

    print(result(a,b,c,d))