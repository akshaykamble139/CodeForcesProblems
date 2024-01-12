guest = input()
host = input()
jumble = input()
expected = {}
for a in guest:
    if a in expected:
        expected[a] += 1
    else:
        expected[a] = 1

for a in host:
    if a in expected:
        expected[a] += 1
    else:
        expected[a] = 1

for a in jumble:
    if a in expected:
        expected[a] -= 1
    else:
        expected[a] = 1

# print(expected.items())
arr = [key for (key,value) in expected.items() if value != 0]
if len(arr) == 0:
    print("YES")
else:
    print("NO")