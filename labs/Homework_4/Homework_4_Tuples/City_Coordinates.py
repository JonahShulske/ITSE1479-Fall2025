"""
Jonah Shulske
October 23, 2025
ITSE-1479 Fall 2025
"""

# Problem 1 - City Coordinates
from hmac import new


dallas = (32.7767, -96.7970)
austin = (30.2672, -97.7431)
houston = (29.7604, -95.3698)
san_antonio = (29.4241, -98.4936)
fort_worth = (32.7555, -97.3308)
hurst = (32.8235, -97.1706)
nrh = (32.8343, -97.2289)

cities = {}
cities.setdefault("Dallas", dallas)
cities.setdefault("Austin", austin)
cities.setdefault("Houston", houston)
cities.setdefault("San Antonio", san_antonio)
cities.setdefault("Fort Worth", fort_worth)
cities.setdefault("Hurst", hurst)
cities.setdefault("North Richland Hills", nrh)

for name, coord in cities.items():
    print(f"{name}, {coord}\n")

while True:
    try:
        city_search = input("Enter a City to Search: ")
        if city_search.isalpha() or " " in city_search:
            city_search = city_search
            break
        else:
            print("Error: City name must be a string.\n")
    except ValueError:
        print("Error: City name must be a string.\n")

try:
    print(f"{city_search}: {cities[city_search]}\n")
except KeyError:
    print(f"Error: {city_search} not found")

while True:
    try:
        choice = input("Add a new city? (y/n): ").lower()
        if choice in ("y", "n"):
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.\n")
    except ValueError:
        print("Invalid input. Please enter 'y' or 'n'.")


if choice == "y":
    while True:
            try:
                new_city = input("Add the city name: ")
                if new_city.isalpha() or " " in new_city:
                    new_city = new_city
                else:
                    print("Error: City name must be a string.\n")
                    continue

                new_coord = input ("Add the coordinates (Format: lon, lat): ")
                lon, lat = map(float, new_coord.split(","))
                cities.setdefault(new_city, (lon, lat))
                if not isinstance(lat, float) or not isinstance(lon, float):
                    print("Error: Coordinates must be floats and follow lon, lat format\n")
                    continue
                else:
                    break
            except ValueError:
                print("Error Adding New City, Try Again\n")
else:
    exit()

for name, coord in cities.items():
    print(f"{name}, {coord}\n")

with open("city_coordinates.txt", "w") as file:
    for name, coord in cities.items():
        file.write(f"{name}: {coord}\n")
    print("\nProgram Complete")
        