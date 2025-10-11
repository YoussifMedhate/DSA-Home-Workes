import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array
from numpy import arange


small_arr = array([1, 3, 5, 7, 8, 11, 34, 43, 100])  # For small test cases and quick timing
big_arr = arange(1, 100_000_001, dtype='int32')    # For a huge test — this will take a long time
big_list = range(1, 100000001)

def ternary_search(arr: array)-> int:
    low = 0
    high = len(arr) - 1
    minIndex = -1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == arr[mid2]:
            low = mid1 + 1
            high = mid2 - 1
            minIndex = mid1

        elif arr[mid1] < arr[mid2]:
            high = mid2 - 1
            minIndex = mid1

        else:
            low = mid1 + 1
            minIndex = mid2

    return minIndex





