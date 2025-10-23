# Standard library
import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array, random

# Example data
small_arr = array([234, 324, 1, 12, 123, -123, 0, 1231, 123, 3234, 43, 122, -1000])
random_arr = random.randint(0, 9999, size=2_000_000)  # large array to show O(n^2) behavior

def insertion_sort(arr: list[int]) -> list[int]:
    """
    Insertion Sort - O(n^2)
    Builds the sorted list one element at a time by inserting
    each new element into its correct position.
    """
    n = len(arr)

    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value

    return arr


print(*small_arr, sep = ", ")
print(*insertion_sort(small_arr), sep = " ,")

print(*random_arr, sep = ", ")
print(*insertion_sort(random_arr), sep = ", ")





               
