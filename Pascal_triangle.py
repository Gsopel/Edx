def generate_pascal_triangle(n):
    if n == 1: return [[1]]

    triangle = [[1], [1, 1]] # pre-populate with the first two rows

    row = [1, 1] # Starts with the second row and calculate the next

    for i in range(2, n):
        row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle

for row in generate_pascal_triangle(6):
    print(row)

