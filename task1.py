with open('input.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))

if len(numbers) != 10:
    raise ValueError("Файл должен содержать ровно 10 чисел")

product = 1
for num in numbers:
    product *= num

with open('output.txt', 'w') as f:
    f.write(str(product))
