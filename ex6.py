num_city = int(input())
num_road = int(input())
map_dict = {}

for _ in range(num_road):
    city_1, city_2, dist = input().split()
    dist = int(dist)
    map_dict[city_1, city_2] = dist

target = input().split()
start = target[0]
end = target[1]

result = {start: 0}
for _ in range(num_city - 1):
    for (city_1, city_2), dist in map_dict.items():
        if city_1 in result and city_2 not in result:
            result[city_2] = result[city_1] + dist
        elif city_2 in result and city_1 not in result:
            result[city_1] = result[city_2] + dist

print(result[end])
