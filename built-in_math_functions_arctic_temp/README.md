# Antarctic Temperatures – Average Calculation

This Python script calculates the **average temperature** from a list of recorded values in Antarctica.  
The result is rounded to **1 decimal place** for readability.

---

# Output screenshot
'screenshots/python_built-in_math_functions.png'

# Step-by-step explanation (line-by-line)

1. Define the data
antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]


A Python list of floats. Each value is a temperature in degrees Celsius.

2. Find the highest temperature

highest_temp = max(antarctic_temperatures)


max() returns the largest value in the list.

For this list, highest_temp becomes -23.8 (the warmest reading).

3. Find the lowest temperature

lowest_temp = min(antarctic_temperatures)


min() returns the smallest value in the list.

For this list, lowest_temp becomes -29.2 (the coldest reading).

4. Print highest and lowest

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")


Displays the values with a unit label for clarity.

5. Calculate the average

average_temp = round(sum(antarctic_temperatures) / len(antarctic_temperatures), 1)


sum(...) adds all list items.

len(...) gives the count of measurements.

Division sum / len produces the average.

round(..., 1) rounds the result to one decimal place for readability (so we get -26.4 instead of a long float like -26.257142857142856).

6. Print the average

print("Average temperature:", average_temp, "°C")


7. Get the absolute value of the coldest reading

coldest_temp_abs = abs(lowest_temp)
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")


abs() converts -29.2 to 29.2, which is useful when saying “X °C below freezing” (positive magnitude).

The message reads naturally: “The coldest temperature was 29.2 °C below freezing.”
