"""

Aditi has used text editing software to type some text. 
After saving the article as words.txt, she realized that she had wrongly
typed the alphabet “J" instead of “I" everywhere in the article.

Write a function definition for JtoI() in Python that would display
the corrected version of the entire content of the file WORDS.TXT
with all the alphabet "J" to be displayed as an alphabet "I" on the screen.

Note: Assume that words.txt does not contain any J alphabet otherwise.

"""

def JtoI(file_name):

    try:
        
        with open(file_name, 'r') as file:
            original_content = file.read()
            corrected_content = original_content.replace('J', 'I')

            return original_content, corrected_content
        
    except FileNotFoundError:

        print(f"File '{file_name}' not found.")
        return None


file_name = "words.txt"
original_content, corrected_content = JtoI(file_name)

print("Original content: ", original_content)
print("Corrected content: ", corrected_content)

