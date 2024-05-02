"""

Write a Python program to count the frequency of each element in a list.
 Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
 Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}

"""

def element_count_frequency(input_list):

    element_frequency_count = {} # Initialize the dictionary

    for element in input_list:
        if element in element_frequency_count:
            element_frequency_count[element] += 1
        else:
            element_frequency_count[element] = 1

    return element_frequency_count

input_numbers = input("Enter list of numbers separated by spaces: ")
input_list = list(map(int, input_numbers.split()))
# input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

frequency_count = element_count_frequency(input_list)

print("Frequency count:", frequency_count)
