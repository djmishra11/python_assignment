"""

Write a Python program to reverse a number using a while loop.

 Sample Input: num = 12345
 Sample Output: revnum = 54321

"""

def reverse_number(num):

    temp = num
    reversed_num = 0

    while (temp != 0):
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp // 10

    return reversed_num

num = int(input("Enter the number for reversing: "))
reversed_number = reverse_number(num)
print(f"The reverse of {num} is {reversed_number}")