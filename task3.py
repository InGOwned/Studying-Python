children = []

with open('children.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()

        surname, name, age = parts
        children.append((surname, name, int(age)))

ages = [age for _, _, age in children]
min_age = min(ages)
max_age = max(ages)

def write_children(filename, target_age):
    with open(filename, 'w') as f:
        for child in children:
            if child[2] == target_age:
                f.write(f"{child[0]} {child[1]} {child[2]}\n")

write_children('youngest.txt', min_age)
write_children('oldest.txt', max_age)