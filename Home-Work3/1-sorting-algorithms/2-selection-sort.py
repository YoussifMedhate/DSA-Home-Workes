# Standard library
import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array, random

# Example data
small_arr = array([234, 324, 1, 12, 123, -123, 0, 1231, 123, 3234, 43, 122, -1000])
random_arr = random.randint(0, 9999, size=2_000_000)  # large array to show O(n^2) behavior


def selection_sort(arr: list[int]) -> list[int]:
    """
    Selection Sort - O(n^2)
    Finds the minimum element in each pass and places it at the correct position.
    Inefficient for large datasets compared to O(n log n) algorithms like Merge Sort or Quick Sort.
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(*small_arr, sep = ", ")
print(*selection_sort(small_arr), sep = " ,")

print(*random_arr, sep = ", ")
print(*selection_sort(random_arr), sep = ", ")
