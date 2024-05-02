"""

Given an array of N integers and an integer K, find the number of 
pairs of elements in the array whose sum is equal to K.

 Sample Input: arr = [1, 2, 3, 4, 5], k = 6
 Sample Output: Pair count: 2

"""

def find_pairs_with_sum_k(array, k):

    array.sort()
    pair_count = 0
    pairs = []
    left_index = 0
    right_index = len(array) - 1

    for left in range(len(array)):
        for right in range(left + 1, len(array)):
            sum = array[left] + array[right]
            if sum == k:
                # print(array[left], array[right])
                pairs.append((arr[left], arr[right]))
                pair_count += 1
                break

    return pairs, pair_count


arr = [1, 2, 3, 4, 5]
k = 6

pairs, count = find_pairs_with_sum_k(arr, k) 
# print(pairs)
print("Pair count: ", count)

