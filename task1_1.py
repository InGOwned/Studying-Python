s = input().strip()

decompressed = []
i = 0

while i < len(s):
    char = s[i]
    i += 1
    num_str = ""
    while i < len(s) and s[i].isdigit():
        num_str += s[i]
        i += 1
    num = int(num_str) if num_str else 1
    decompressed.append(char * num)
    
print("".join(decompressed))