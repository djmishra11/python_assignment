"""

Write a Python program to find the sum of all odd numbers between two given numbers. 
    - Start = 1, stop = 10
    - Sum of odd numbers: 25

"""

def odd_numbers_sum(begin, end):
    total = 0
    for num in range(begin, end + 1):
        if num % 2 != 0:
            total += num
    return total

# start = 1
# stop = 10

start = int(input("Enter the starting number: "))
stop = int(input("Enter the ending number: "))

result_sum = odd_numbers_sum(start, stop)
print(f"Sum of odd numbers between {start} and {stop}: {result_sum}")
