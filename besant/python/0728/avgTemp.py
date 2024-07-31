"""
Problem: Calculate and print the average temperature for a week based on user input.
"""
temperatures = []

for i in range(1, 8):
    temp = float(input(f"enter the temperature for day {i} : "))
    temperatures.append(temp)

add = 0
for temp in temperatures:
    add += temp
count = len(temperatures)
avg = add/count

print(f"The average temperature for the week: {avg:.2f}")
