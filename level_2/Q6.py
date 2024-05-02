"""

Write a Python program to check if a number is a power of two using recursion.

"""

def check_if_power_of_two(num):
    
    if num == 1:
        return True
    elif num % 2 != 0 or num == 0:
        return False
    else:
        return check_if_power_of_two(num // 2)


num = int(input("Enter a number: "))

if check_if_power_of_two(num):
    print(num, "is a power of two.")
else:
    print(num, "is not a power of two.")
