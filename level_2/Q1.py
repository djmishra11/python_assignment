"""

Write a Python program to find the common elements between two lists.

 Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
 Sample output: [4, 5]

"""

def find_common_elements_in_lists(list1, list2):

    common_elements = []

    for i in list1:
        for j in list2:
            if i == j:
                common_elements.append(i)

    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(find_common_elements_in_lists(list1, list2))



"""

This code accounts for duplicates in the list.
The above code will have duplicates appended if there is repeated
common element between two lists.


def find_common_elements_in_lists(list1, list2):

    common_elements = set() # Stores only unique common elements

    for i in list1:
        for j in list2:
            if i == j:
                common_elements.add(i)

    return list(common_elements)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 5, 6, 7, 8]

print(find_common_elements_in_lists(list1, list2))


"""
