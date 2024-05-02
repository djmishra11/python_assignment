"""

You need to write a function that accepts an encoded string as a parameter. 
This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. 
The id is a numeric value but will contain no zeros. 
The function should parse the string and return a Python dictionary that contains the
first name, last name, and id values.

 For example:
 Input : “Robert000Smith000123”
 Output: { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

"""

def parse_encoded_string(encoded_string):
    
    components = encoded_string.split('0')
    components = [component for component in components if component] # Remove empty components

    first_name = components[0]
    last_name = components[1]
    id_number = components[2]

    parsed_values = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_number
    }

    return parsed_values


encoded_string = "Robert000Smith00000123"
parsed_values = parse_encoded_string(encoded_string)

print("Input:", encoded_string)
print("Output:", parsed_values)
