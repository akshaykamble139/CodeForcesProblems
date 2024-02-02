n = int(input())

total = 0
least_cost = 101

for i in range(n):
    word = [int(a) for a in input().split()]
    meat_required = word[0]
    cost_of_meat = word[1]
    if cost_of_meat < least_cost:
        least_cost = cost_of_meat
    total += least_cost*meat_required

print(total)

