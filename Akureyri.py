n = int(input())
cities = {}

for i in range(n):
    name = input()
    city = input()
    if cities.get(city):
        cities[city] += 1
    else:
        cities[city] = 1

sorted_cities = sorted(cities.items())

for key, value in sorted_cities:
    print(key, value)
