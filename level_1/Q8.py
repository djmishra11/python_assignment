"""

Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
 
 number1 = 12, number2 = 18
 LCM of 12 and 18 are: 36

"""

import math

def lcm(num1, num2):
    return (num1 * num2) // math.gcd(num1, num2)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

lcm_result = lcm(number1, number2)
print(f'LCM of {number1} and {number2} are: {lcm_result}')


