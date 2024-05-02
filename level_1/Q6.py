"""

Write a Python program to check if a given number is a perfect number.


- A Perfect number is a positive integer that is equal to the sum of
 its proper divisors. For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +
 3 = 6, so 6 is a perfect number.

 Input: 5 
 Output: No

"""

# A perfect number is a positive integer that is equal to the sum of its positive divisors,
# excluding the number itself

def find_perfect_number(num):

    if num <= 0:
        return False
    
    divisors_sum = 0

    for i in range(1, num // 2 + 1): # Checking for half of the given number
        if num % i == 0:
            divisors_sum += i
    
    return divisors_sum == num


num = int(input("Enter a number: "))

if find_perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
