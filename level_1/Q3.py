"""

Write a Python program to input marks for five subjects Physics,
Chemistry, Biology, Mathematics, and Computer. Calculate the
percentage and grade according to the following:

 - Percentage >= 90% : Grade A
 - Percentage >= 80% : Grade B
 - Percentage >= 70% : Grade C
 - Percentage >= 60% : Grade D
 - Percentage >= 40% : Grade E
 - Percentage < 40% : Grade F

"""

# This code assumes that each subject marks are capped at maximum of 100 points
# Range 0-100 for marks

marks_Physics = int(input("Enter the marks for Physics subject (range: 0-100): "))
marks_Chemistry = int(input("Enter the marks for Chemistry subject (range: 0-100): "))
marks_Biology = int(input("Enter the marks for Biology subject (range: 0-100): "))
marks_Mathematics = int(input("Enter the marks for Mathematics subject (range: 0-100): "))
marks_Computer = int(input("Enter the marks for Computer subject (range: 0-100): "))

obtained_Marks = marks_Physics + marks_Chemistry + marks_Biology + marks_Mathematics + marks_Computer

percentage = (obtained_Marks / 500) * 100

if percentage >= 90:
    print(f"Obtained Marks: {obtained_Marks}, Obtained Percentage: {percentage}, Result: Grade A")

elif percentage >= 80:
    print(f"Obtained Marks: {obtained_Marks}, Obtained Percentage: {percentage}, Result: Grade B")

elif percentage >= 70:
    print(f"Obtained Marks: {obtained_Marks}, Obtained Percentage: {percentage}, Result: Grade C")

elif percentage >= 60:
    print(f"Obtained Marks: {obtained_Marks}, Obtained Percentage: {percentage}, Result: Grade D")

elif percentage >= 40:
    print(f"Obtained Marks: {obtained_Marks}, Obtained Percentage: {percentage}, Result: Grade E")

else:
    print(f"Obtained Marks: {obtained_Marks}, Obtained Percentage: {percentage}, Result: Grade F")