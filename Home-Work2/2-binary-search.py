# Standard library
import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array

small_arr = array([1, 3, 5, 7, 8, 11, 34, 43, 100])  # For small test cases and quick timing
big_arr = array([x for x in range(1, 100000001)])    # For a huge test — this will take a long time
big_list = [x for x in range(1, 100000001)]


def binary_search(arr: array, element: int) -> int:
    """
    Binary Search:
    First, we initialize 'left' as 0 and 'right' as len(array) - 1.
    Then we check if the target equals the middle element:
        - If yes, return its index.
        - If no:
            1. If target > middle → move 'left' to middle + 1
            2. If target < middle → move 'right' to middle - 1
    Repeat these steps until the element is found.
    If the target is not found, return -1.

    Worst-case time complexity: O(log n)
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (right + left) // 2

        if arr[middle] == element:
            return middle
        elif arr[middle] < element:
            left = middle + 1
        else:
            right = middle - 1

    return -1

# 1- Small test
start = time.time()
print(binary_search(small_arr, 100))
end = time.time()
print(f'Small array took -> {end - start} seconds')

print('-' * 80)

# 2- Big test with NumPy array
start = time.time()
print(binary_search(big_arr, 100000000))
end = time.time()
print(f'Big array took -> {end - start} seconds')
# Takes longer because NumPy doesn't handle comparison operators as efficiently as Python lists.
# For very large arrays, linear operations in NumPy may sometimes perform better,
# but with regular Python lists, binary search is definitely faster.

print('-' * 80)

# 3- Big test with Python list
start = time.time()
print(binary_search(big_list, 100000000))
end = time.time()
print(f'Big list took -> {end - start} seconds')
# In this case, you can clearly see the power of binary search —
# it’s much faster than linear search and faster than using NumPy arrays for this operation.

# I tried to follow PEP 8 formatting guidelines.
# Binary Search — DONE :)
