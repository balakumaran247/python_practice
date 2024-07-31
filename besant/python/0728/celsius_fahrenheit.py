"""
Problem: Convert a list of temperatures from Celsius to Fahrenheit and calculate the average temperature in Fahrenheit for a week.
"""
total = int(input("total number of values you are going to enter: "))

temperatures = []
for _ in range(total):
    temp = float(input("enter the temperature in celsius: "))
    temperatures.append(temp)

fahrenheit = []
for c in temperatures:
    f = ((9/5)*c)+32
    fahrenheit.append(f)

add = 0
for j in fahrenheit:
    add += j
count = len(fahrenheit)
avg = add/count

print(f"The average temperature in fahrenheit: {avg:.2f}")
