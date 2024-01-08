n_and_k = input()
arr = n_and_k.split()
n = int(arr[0])
k = int(arr[1])

values = input()
values_list =[int(n) for n in values.split()]
cutoff = values_list[k-1]

next_round = [n for n in values_list if n >= cutoff and n > 0]
print(len(next_round))
