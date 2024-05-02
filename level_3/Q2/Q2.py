"""

Write a program to count the lines in a file “demo.txt”

"""

def count_lines_in_file(file_name):

    try:
    
        with open(file_name, 'r') as file:
            line_count = 0

            for line in file:
                line_count += 1
            
            return line_count
        
    except FileNotFoundError:

        print(f"File '{file_name}' not found.")
        return None


file_name = "demo.txt"
lines_count = count_lines_in_file(file_name)
if lines_count is not None:
    print(f"Number of lines in '{file_name}':", lines_count)
