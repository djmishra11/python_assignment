"""

Create a function that takes a list and returns a new list with 
unique elements of the first list.

 Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
 Sample Output: list2 = [1, 2, 3, 4, 5]

"""

def find_unique_elements_in_list(list):

    unique_elements = []

    for i in list:
        if i not in unique_elements:
            unique_elements.append(i)

    return unique_elements


original_list = [1, 2, 2, 3, 4, 4, 5, 5]
print("Unique elements list: ", find_unique_elements_in_list(original_list))
