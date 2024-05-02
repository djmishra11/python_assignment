"""

Write a program to construct a dictionary from the two lists containing the names of 
students and their corresponding subjects. 

The dictionary should map the students with their respective subjects. 
Let us see how to do this using for loops and dictionary comprehension.

 Input: [Sam, Alice, Mona] , 
        [Commerce, Science, Computer]
 Output:   [Sam: Commerce,  Alice: Science , Mona: Computer]

"""

student_names = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

student_subject_dict = {name: subject for name, subject in zip(student_names, subjects)}

print("Output:", student_subject_dict)
