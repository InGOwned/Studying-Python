s = input().strip()

if not s:
    print("")

else:
    compressed = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + (str(count) if count > 1 else ""))
            current_char = char
            count = 1
    
    compressed.append(current_char + (str(count) if count > 1 else ""))
    
    print("".join(compressed))
