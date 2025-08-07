celsius_temperatures = [] # Start with an empty list
fahrenheit_temperatures = []

celsius = [0, 10, 25, 32, 100]
celsius_temperatures = celsius

for celsius in celsius_temperatures:
    fahrenheit = (celsius * 9/5) + 32

    fahrenheit_temperatures.append(fahrenheit)

# Print both lists (do not modify)
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures) 
