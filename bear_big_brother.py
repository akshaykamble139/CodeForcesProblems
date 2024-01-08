l_b = input()
arr = l_b.split()
limak = int(arr[0])
bob = int(arr[1])

years = 0
while limak <= bob:
    years += 1
    limak *= 3
    bob *= 2

print(years)