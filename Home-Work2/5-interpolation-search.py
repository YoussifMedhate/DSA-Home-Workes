import time  # Used for measuring execution time (not the most accurate method)

# Third-party
from numpy import array
from numpy import arange


small_arr = array([1, 3, 5, 7, 8, 11, 34, 43, 100])  # For small test cases and quick timing
big_arr = arange(1, 100_000_001, dtype='int32')    # For a huge test — this will take a long time
big_list = range(1, 100000001)


def interpolation_search(arr: array, target: int)->int:
    low = 0
    high = len(arr) - 1


    if low == high:
        return 0 if arr[0] == target else -1
    
    while low <= high and target >= arr[low] and target <= arr[high]:

        index = int(low + ((high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        element = arr[index]
        
        if element == target:
            return index
        
        elif element < target:
            low = index + 1

        else:
            high = index - 1

    return -1


start = time.time()

print(interpolation_search(big_arr, 88888))

end = time.time()


print(f'time --> {end - start}')
