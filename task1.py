lst = list(map(int, input().split()))

min_val, max_val = min(lst), max(lst)
min_idx, max_idx = lst.index(min_val), lst.index(max_val)
lst[min_idx], lst[max_idx] = max_val, min_val

print(lst)