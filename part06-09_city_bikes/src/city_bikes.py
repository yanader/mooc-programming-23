import math

def get_station_data(filename: str):
    station_dict = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            station_dict[parts[3]] = (float(parts[0]),float(parts[1]))
    return station_dict

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    greatest_distance = 0.0
    greatest_station1 = ''
    greatest_station2 = ''
    for station1 in stations.keys():
        for station2 in stations.keys():
            if distance(stations, station1, station2) > greatest_distance:
                greatest_distance = distance(stations, station1, station2)
                greatest_station1 = station1
                greatest_station2 = station2
    return (greatest_station1, greatest_station2, greatest_distance)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)