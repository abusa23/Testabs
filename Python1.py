

"""
A recursive function that computes ab for given numbers a and b, where b is an integer. No use of ** .
"""
def product(a, b):
    # Base case: if b is 0, the product is 0
    if b == 0:
        return 0
    # Recursive case: add 'a' to the product of (a, b-1)
    return a + product(a, b - 1)


a = 9
b = 6
result = product(a, b)
print(f"The product of {a} and {b} is: {result}")
"""
This recursive function repeatedly adds a to the product of 
a and b-1 until b becomes 0, at which point the base case is reached,
 and the recursion stops.
"""


print("\n")

""" ================================================================================"""


"""
Two functions, one that uses iteration, and the other using recursion, that achieve the fol-
lowing:
The input of the function is a list with numbers. The functions return the product of the numbers
in the list.
"""


# Using Recursion

def product_recursive(numbers):
    # Base case: if the list is empty, the product is 1
    if not numbers:
        return 1
    # Recursive case: product = first element * product of the rest of the list
    else:
        return numbers[0] * product_recursive(numbers[1:])

number_list = [6, 7, 8, 9]
result_recursive = product_recursive(number_list)
print("Product (Recursive):", result_recursive)


# Using Iteration

def product_iterative(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

number_list = [6, 7, 8, 9]
result_iterative = product_iterative(number_list)
print("Product (Iterative):", result_iterative)

print("\n")

""" ================================================================================"""

"""
A Python function which takes a list of numbers and returns the:
a. median
b. mean
"""

def calculate_median_mean(numbers):
    # Ensure the list is not empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Sort the list for median calculation
    sorted_numbers = sorted(numbers)

    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate median
    n = len(sorted_numbers)
    if n % 2 == 0:
        # If the list has an even number of elements, take the average of the middle two
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # If the list has an odd number of elements, the median is the middle element
        median = sorted_numbers[n // 2]

    return median, mean

numbers = [8, 12, 3, 13, 7, 1]
median, mean = calculate_median_mean(numbers)
print("Median:", median)
print("Mean:", mean)


print("\n")

""" ================================================================================"""

"""
A function which takes a Python dictionary and returns two NumPy arrays, one con-
taining the keys and one containing the values. The keys and values are in corresponding
order.
"""

import numpy as np

def dict_to_numpy_arrays(input_dict):
    # Extract items (key-value pairs) from the dictionary
    items = list(input_dict.items())

    # Separate keys and values into two lists
    keys, values = zip(*items)

    # Convert lists to NumPy arrays
    keys_array = np.array(keys)
    values_array = np.array(values)

    return keys_array, values_array


my_dict = {'Henry': 0, 'Jane': 1, 'Tom': 2}
keys_array, values_array = dict_to_numpy_arrays(my_dict)

print("Keys Array:", keys_array)
print("Values Array:", values_array)

print("\n")

""" ================================================================================"""


"""
A function named dif2 accepts an integer N as input parameter and constructs and
returns an N x N two-dimensional numpy array A, with the value -1.0 on the main/major diagonal.
"""


def dif2(N):
    # Create an N x N array filled with 0.0
    A = np.full((N, N), 0.0)
    
    # Set the main/major diagonal elements to -1.0
    np.fill_diagonal(A, -1.0)
    
    return A

N = 6
result = dif2(N)
print(result)


