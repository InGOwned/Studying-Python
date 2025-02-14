n = int(input("Введите число строк: "))
triangle = []

for i in range(n):
    row = [1]
    if i > 0:
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
    triangle.append(row)

for i in range(n):
    space = ' ' * (n - i - 1)
    print(space + ' '.join(map(str, triangle[i])))