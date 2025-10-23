# Standard library
import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array
from numpy import random

small_arr = array([234, 324, 1, 12, 123, -123, 0, 1231, 123, 3234, 43, 122 , -1000])  
random_arr = random.randint(0, 9999, size= 2_000_000) #  large array to show O(n^2) behavior

def bubble_sort(arr: list[int]) -> list[int]:
    """Bubble Sort - O(n^2)
    Compares each two elements and swaps them if the first is bigger than the second.
    Not efficient for large datasets.
    """
    n =  len(arr)
    for i in range(0 , n - 1):
        is_swaped = False
        for j in range(0 , n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swaped = True
        if not is_swaped:
            break
            
    return arr


print(*small_arr, sep = ", ")
print(*bubble_sort(small_arr), sep = " ,")

print(*random_arr, sep = ", ")
print(*bubble_sort(random_arr), sep = ", ")
