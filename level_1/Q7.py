"""

Write a Python program to check if a string is an anagram of another string.

 string1 = "listen", string2 = "silent"
 Output: True

"""

def string_anagram_check(string1, string2):

    # Remove spaces and convert to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if striings are of equal length
    if len(string1) != len(string2):
        return False
    
    # Use sorted function to sort the strings and then compare
    return sorted(string1) == sorted(string2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print(string_anagram_check(string1, string2))

