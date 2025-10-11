import numpy as np
arr = np.array([1, 2, 3, 4, 5, 64, 77, 79, 86])
arr2 = np.array([x for x in range(1000)]) # use this expretion to creat big array

print(*arr , sep=', ') #print array
print(arr.ndim) #for know array dimintion


