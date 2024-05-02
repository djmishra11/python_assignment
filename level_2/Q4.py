"""

Given an array of size N. The task is to rotate array by D elements towards right.

 Sample Input: arr = [1, 2, 3, 4, 5], D = 2
 Sample Output: arr after rotation = [4, 5, 1, 2, 3]

"""

def rotate_array_by_D(array, D):

    # n = len(arr)

    if D == 0:
        return array
    
    rotated_array = array[-D:] + array[:-D]

    return rotated_array

array = [1, 2, 3, 4, 5]
D = 2

rotated_array = rotate_array_by_D(array, D)

print("Array after rotation:", rotated_array)
