n = input()


def check_nearly_lucky(num):
    count = 0
    for i in range(len(num)):
        if num[i] == '4' or num[i] == '7':
            count += 1

    return count


lucky_count = check_nearly_lucky(n)
if check_nearly_lucky(str(lucky_count)) == len(str(lucky_count)):
    print("YES")
else:
    print("NO")