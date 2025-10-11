# Standard library
import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array

small_arr = array([1, 3, 5, 7, 8, 11, 34, 43, 100])  # For small test cases and quick timing
big_arr = array([x for x in range(1, 100000001)])    # For a huge test — this will take a long time
big_list = [x for x in range(1, 100000001)]


def jump_search(arr: array, target: int, jump_value=None) -> int:
    """
        Jump Search:
        First, we choose a jump size (usually √n, where n is the array length).
        We start from index 0 and jump ahead by that step size each time:
            - If the target is greater than the current element, 
              move the jump window forward.
            - If the target is smaller or we've passed its possible position,
              stop jumping — the target must be in the previous block.
        
        Then, perform a linear search within that block 
        (from the previous jump point to the current one).

        If the target is found, return its index.
        If not, return -1.

        Worst-case time complexity: O(√n)
    """

    number_of_element = len(arr)
    
    if number_of_element == 0:
        raise MemoryError("There are no element in the array")

    if jump_value is None:
        jump_value = int(number_of_element ** 0.5)

    if jump_value <= 0:
        raise ValueError(f"jump_value = {jump_value} and it isn't logical becouse jump_value must be bigger than 0")
    
    prv = 0
    cur = jump_value

    while cur < number_of_element:
        if target == arr[cur]:
            return cur
        elif target > arr[cur]:
            prv = cur
            cur += jump_value
        elif arr[cur] > target:
            break

    for i in range(prv, min(cur, number_of_element)):
        if arr[i] == target:
            return i
    
    return -1

# 1- Small test
start = time.time()
print(jump_search(small_arr, 100, 0))
end = time.time()
print(f'Small array took -> {end - start} seconds')

print('-' * 80)

# 2- Big test with NumPy array
start = time.time()
print(jump_search(big_arr, 100000000))
end = time.time()
print(f'Big array took -> {end - start} seconds')
# Jump Search is efficient for sorted arrays when random access is allowed.
# However, NumPy arrays can be slightly slower in this case,
# because element-by-element comparisons in NumPy have some overhead.

print('-' * 80)

# 3- Big test with Python list
start = time.time()
print(jump_search(big_list, 100000000, -1))
end = time.time()
print(f'Big list took -> {end - start} seconds')
# In this case, you can clearly see how Jump Search performs better than
# a pure linear search on large sorted lists.
# However, for very large datasets, Binary Search is still faster
# because it reduces the search space exponentially (O(log n) vs O(√n)).

# I tried to follow PEP 8 formatting guidelines.
# Jump Search — DONE :)
