"""
Question 3: City Population Analysis
Description:
You have a list of cities with their populations and areas. You need to calculate the population density for each city and identify the city with the highest population density.

Task:
Create a list of tuples where each tuple contains a city's name, population, and area.
Calculate the population density for each city and store it in a dictionary.
Find the city with the highest population density.
"""
details = [
    ('chennai', 1600000, 2000000),
    ('mumbai', 2200000, 1800000),
    ('jaipur', 1200000, 2200000)
]

pop_dict = {}
for i in details:
    name, pop, area = i
    pop_dict[name] = pop/area

final_name = None
final_density = 0

for name, density in pop_dict.items():
    if density > final_density:
        final_name = name
        final_density = density

print(f"the city with highest population: {final_name}")
