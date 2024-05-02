"""

Write a Python function that finds the median of a list of numbers.

 Sample Input: number_list = [7, 2, 5, 1, 9, 3]
 Sample Output: Median: 4.0


"""

def find_median_number(num_list):
    
    sorted_list = sorted(num_list)
    n = len(sorted_list)

    # Determine the middle element
    if n % 2 == 1:  # Odd number of elements  --> median simply the middle element
        median = sorted_list[n // 2]
    else:  # Even number of elements  --> median is average of two middle elements
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

    return median


number_list = [7, 2, 5, 1, 9, 3]
median = find_median_number(number_list)

print("Median: ", median)
