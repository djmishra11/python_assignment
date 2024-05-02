"""

Write a Python program to find the factorial of a number using a for loop.

"""

def find_factorial(num):

    if num < 0:
        raise ValueError("Factorial cannot be calculated for negative numbers")
    
    elif num == 0 or num == 1:
        return 1
    
    else:
        factorial_product = 1
        for i in range(2, num + 1):
            factorial_product = factorial_product * i
        return factorial_product
    
num = int(input("Enter the number to find the factorial: "))
factorial_output = find_factorial(num)

print(f'The factorial of {num} is: {factorial_output}')