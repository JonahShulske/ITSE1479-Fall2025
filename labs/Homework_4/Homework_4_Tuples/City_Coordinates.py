"""
Jonah Shulske
October 23, 2025
ITSE-1479 Fall 2025
"""

# Problem 1 - City Coordinates
cities = {
    "Dallas": (32.7767, -96.7970),
    "Austin": (30.2672, -97.7431),
    "Houston": (29.7604, -95.3698),
    "San Antonio": (29.4241, -98.4936),
    "Fort Worth": (32.7555, -97.3308),
    "Hurst": (32.8235, -97.1706),
    "North Richland Hills": (32.8343, -97.2289)}

for name, coord in cities.items():
    print(f"{name}, {coord}\n")

city_search = input("Enter a City to Search: ")

try:
    print(f"{city_search}: {cities[city_search]}\n")
except KeyError:
    print(f"Error: {city_search} not found")

choice = input("Add a new city? (y/n): ").lower()

if choice == "y":
    new_city = input("Add a new city: ")
    new_coord = input ("Add the coordinates: ")
    temp_dict = {new_city: f"({new_coord})"}
    cities.update(temp_dict)
else:
    exit()

for name, coord in cities.items():
    print(f"{name}, {coord}\n")