file_name = "earthquake.txt"
earth_quake_city_data = {}
with open(file_name, "r") as fh:
    for line in fh:
        data = line.split()
        earth_quake_data = [data[0], data[1]]
        if data[-1] not in earth_quake_city_data:
            earth_quake_city_data[data[-1]] = []
            earth_quake_city_data[data[-1]].append(earth_quake_data)
    result = []

    for key in earth_quake_city_data:
        city_result = []
        city_result.append(key)
        city_result.extend(earth_quake_city_data[key])
        result.append(city_result)
    print result