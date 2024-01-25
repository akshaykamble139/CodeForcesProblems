n = int(input())

encoded = input()

decoded = ""

add_at_start = False

if n%2 == 0:
    add_at_start = True

for a in encoded:
    if add_at_start:
        decoded = a + decoded
    else:
        decoded += a
    add_at_start = not add_at_start

print(decoded)

