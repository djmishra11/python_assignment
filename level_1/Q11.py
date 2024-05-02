"""

Write a Python program to calculate the sum of digits of a given
number until the sum becomes a single-digit number.

 Sample Input: num = 987
 Sample Output: Sum_of_digits = 24,
 Again compute the sum of digits so that it can be reduced to
 on single digit.
 Final Output: 6


"""

def compute_digits_sum(num):
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        num = digit_sum
    return num


num = int(input("Enter a number: "))
digits_sum = compute_digits_sum(num)

print("Sum of digits of a number until it becomes a single-digit number: ", digits_sum)