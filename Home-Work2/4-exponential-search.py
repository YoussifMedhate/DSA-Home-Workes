#Standard library
import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array
from numpy import arange

small_arr = array([1, 3, 5, 7, 8, 11, 34, 43, 100])  # For small test cases and quick timing
big_arr = arange(1, 100_000_001, dtype='int32')    # For a huge test — this will take a long time
big_list = range(1, 100000001)

def binary_search_special_case(arr: array, left: int, right: int , target: int)-> int:

   while left <= right:
      middle = (right + left) // 2
      if arr[middle] == target:
         return middle
      
      elif arr[middle] < target:
         left = middle + 1 
      
      elif arr [middle] > target:
         right = middle - 1

   return -1
         


def exponential_search(arr: array, target: int) -> int:
    number_of_elements = len(arr)
    
    if number_of_elements == 0:
       return -1
    
    if arr[0] == target:
       return 0
    
    i = 1
    while i < number_of_elements and arr[i] <= target:
        i *= 2

    
    left = i // 2
    right = min(number_of_elements - 1, i)
    
    return binary_search_special_case(arr, left, right, target)



start = time.time()

print(exponential_search(big_arr, 645785785757855))

end = time.time()

print(f'take -> {end - start}')
