"""

Write a program that accepts a string as input from the user and
calculates the number of digits and letters.

    - Input: Hello123 
    - Output: Alphabets: 5 & Number : 3

"""

def count_letters_digits(string):

    num_digits = 0
    num_letters = 0
    num_other = 0
    # digits = []
    # letters = []
    # other = []

    for char in string:

        if char.isdigit():
            num_digits += 1
            # digits.append(char)

        elif char.isalpha():
            num_letters += 1
            # letters.append(char)

        else:
            num_other += 1
            # other.append(char)

    return num_digits, num_letters

    # return num_digits, num_letters, num_other, digits, letters, other

# Accept input from the user
user_input = input("Enter a string: ")

# Count and categorize the characters
digits_count, letters_count = count_letters_digits(user_input)
# digits_count, letters_count, other_count, digits, letters, other = count_letters_digits(user_input)

# Display the counts
print("Number of digits:", digits_count)
print("Number of letters:", letters_count)
# print("Number of other characters:", other_count)

# Display the characters
# print("Digits: ", digits)
# print("Letters: ", letters)
# print("Other characters: ", other)

# Display the characters
# print("Digits:", ''.join(digits))
# print("Letters:", ''.join(letters))
# print("Other characters:", ''.join(other))

