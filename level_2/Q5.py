"""

You are developing a program that analyzes weather data. 

Write a Python function that takes a list of temperature readings for a specific location 
and determines the average temperature, highest temperature, and lowest temperature.

 Input: temperature_readings = [25, 28, 21, 24, 27]
 Output: Average Temperature: 25.0
         Highest Temperature: 28
         Lowest Temperature: 21

"""

# temperature_readings = [25, 28, 21, 24, 27]

input_temperature_readings = input("Enter the temperature readings separated by spaces: ")
temperature_readings = list(map(int, input_temperature_readings.split()))

average_temp = sum(temperature_readings) / len(temperature_readings)
highest_temp = max(temperature_readings)
lowest_temp = min(temperature_readings)

print(f'Avergae Temperature: {average_temp}')
print(f'Highest Temperature: {highest_temp}')
print(f'Lowest Temperature: {lowest_temp}')