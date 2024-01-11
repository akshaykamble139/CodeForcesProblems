n = int(input())

faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

count = 0
while n > 0:
    n -= 1
    word = input()
    count += faces[word]

print(count)