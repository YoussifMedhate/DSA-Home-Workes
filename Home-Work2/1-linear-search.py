#Standard library
import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array

small_arr = array([1, 3, 5, 7, 8, 11, 34, 43, 100])  # For small test cases and quick timing
big_arr = array([x for x in range(1, 100000001)])    # For a huge test — this will take a long time


def linear_search(arr: array, target: int) -> int: 
    """
    Linear Search:
    It goes through every element in the array from index 0 up to the target.
    If it finds the target -> returns its index, otherwise returns -1.
    
    Worst-case time complexity: O(N)
    """
    for index, element in enumerate(arr): # traverse to access each element
        if element == target: # check the element == target or not
            return index
    return -1


# Small test
start = time.time()
print(linear_search(small_arr, 100))
end = time.time()
print(f'Small array took -> {end - start} seconds')

print('-' * 80)

# Reusing the same variable name doesn’t actually save memory in Python,
# but it does in lower-level languages like C++ & C.
# (In Python, only integers between -5 and 256 are cached and reused.)

# Big test
start = time.time()
print(linear_search(big_arr, 100000000))
end = time.time()

print(f'Big array took -> {end - start} seconds')  # Takes a long time,
# other algorithms are faster for searching


# I tried to write the code using PEP8 format
# Linear search DONE :)
