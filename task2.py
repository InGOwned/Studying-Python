def sierpinski(n):
    if n == 0:
        return ['*']
    
    prev = sierpinski(n - 1)

    space = ' ' * (2 ** (n - 1))

    top = [space + line + space for line in prev]
    bottom = [line + ' ' + line for line in prev]

    return top + bottom

for line in sierpinski(6):
    print(line)
