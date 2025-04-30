with open('input_2.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]

sorted_numbers = sorted(numbers)

with open('output_2.txt', 'w') as f:
    for num in sorted_numbers:
        f.write(f"{num}\n")