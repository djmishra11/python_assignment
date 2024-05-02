"""

Given an input string, write a function that returns the run 
length encoded string for the input string.

 For Example:
 Input: wwwwaaadebbbbbw
 Output: w4a3d1e1b5w1

"""

def run_length_encoding_string(input_string):
    
    encoded_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + str(count)
            count = 1

    encoded_string += input_string[-1] + str(count)
    
    return encoded_string


input_string = "wwwwaaadebbbbbw"
encoded_string = run_length_encoding_string(input_string)

print("Input:", input_string)
print("Output:", encoded_string)
