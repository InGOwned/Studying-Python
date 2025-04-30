strings = input().split()

unique_strings = []
counts = {}

for s in strings:
    if s not in counts:
        unique_strings.append(s)
        counts[s] = 1
    else:
        counts[s] += 1

result = [str(counts[s]) for s in unique_strings]

print(' '.join(result))
