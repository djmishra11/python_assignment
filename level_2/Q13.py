"""

Write a Python program to find if a given string starts with a given character using Lambda.

 Sample input: input_string = "Hello, World!", given_char = "H"
 Sample Output: True

"""

# input_string = "Hello, world!"
# given_char = "H"

input_string = input("Enter the string: ")
given_char = input("Enter the starting character: ")

result = lambda string, char: string.startswith(char)

print(result(input_string, given_char))
