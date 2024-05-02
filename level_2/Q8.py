"""

 Write a Python function that counts the number of vowels in a given string.

 Sample Input: string = "Hello, World!"
 Sample Output: Number of vowels: 3


"""

string = input("Enter the string: ")
vowels_count = 0
vowels_list = ['a', 'e', 'i', 'o', 'u']

for char in string:
    if char in vowels_list:
        vowels_count += 1

print("Number of Vowels: ", vowels_count)
