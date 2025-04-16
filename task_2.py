
set1_input = input()
set1 = set(map(int, set1_input.split()))

set2_input = input()
set2 = set(map(int, set2_input.split()))

is_subset = set1.issubset(set2) and (set1 != set2)

print(is_subset)
