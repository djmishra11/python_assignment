"""

Write a Python program to create a list of given strings individually of the list 
using the Python map function.
 
 Eg.: Input: ['Red', 'Blue', 'Black', 'White', 'Pink'] 
      Output: [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], 
              ['W', 'h', 'i', 't', 'e'], ['P', 'i','n', 'k']]

"""

input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']

output_lists = list(map(list, input_list))

print("Output:", output_lists)
