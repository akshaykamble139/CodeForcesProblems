n = int(input())
word = input()

count_dict = {}
max_val = 1
max_str = word[0:2]
for i in range(n-1):
    string = word[i:i+2]
    if string in count_dict:
        count = count_dict[string]
        count += 1
        count_dict[string] = count
        if count > max_val:
            max_val = count
            max_str = string
    else:
        count_dict[string] = 1

print(max_str)


