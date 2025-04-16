n = int(input())
cities = set()

for _ in range(n):
    city = input()
    cities.add(city)

new_city = input()

print("REPEAT" if new_city in cities else "OK")
