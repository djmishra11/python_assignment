"""

Write a Python program that executes an operation on a list and
handles an IndexError exception if the index is out of range.
 
"""

def print_element_from_list(list, index):

    try:
        result = list[index]
        print("Element at index", index, ":", result)

    except IndexError:
        print("Index", index, "is out of range for the list.")


list = [1, 2, 3, 4, 5]
index = int(input("Enter the index of the element to print: "))

print_element_from_list(list, index)
