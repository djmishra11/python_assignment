"""

Write a Python program to reverse the order of words in a given sentence.

 Input_sentence = “Hello, World! Welcome to Python programming.”
 Output after reverse = “programming. Python to Welcome World! Hello,”

 
"""

def reverse_word_order_in_sentence(sentence):

    # Split the sentence into words
    words = sentence.split()

    # Use slicing to reverse the order of words
    reversed_words = words[::-1]

    reversed_word_order_sentence = ' '.join(reversed_words)

    return reversed_word_order_sentence

input_sentence = input("Enter the sentence: ")
reversed_word_order_sentence = reverse_word_order_in_sentence(input_sentence)

print("Output after reverse:", reversed_word_order_sentence)
