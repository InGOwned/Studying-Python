s = input().strip().replace(" ", "")

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1
    
sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

for i in range(min(3, len(sorted_chars))):
    print(f"{sorted_chars[i][0]} {sorted_chars[i][1]}")