"""

 Read the doc.txt file using Python File handling concept and
 return only the even length string from the file. Consider the
 content of doc.txt as given below:
 Hello I am a file
 Where you need to return the data string which is of even length.
 Make sure you return the content in The same link as it is present.
 
"""

def return_even_length_strings(file_name):

    try:
        
        with open(file_name, 'r') as file:
            read_content = file.read()
            words = read_content.split()

            # Check for even length words
            even_length_words = [word for word in words if len(word) % 2 == 0]
            result = ' '.join(even_length_words)

            return result
        
    except FileNotFoundError:

        print(f"File '{file_name}' not found.")
        return None


file_name = "doc.txt"
even_length_strings = return_even_length_strings(file_name)

if even_length_strings:
    print("Even length strings from the doc.txt file: ", even_length_strings)


