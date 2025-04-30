numbers = list(map(int, input().split()))

result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]

print(result)