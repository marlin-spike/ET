#practical 3

#numpy

import numpy as np
arr = np.array([[[1, 2, 3],
                 [4, 2, 5]]])
print("Array is of type: ", type(arr))
print("\nNo. of dimensions: ", arr.ndim)
print("\nShape of array: ", arr.shape)
print("\nSize of array: ", arr.size)
print("\nArray stores elements of type: ", arr.dtype)
print("\n\nArray elements in sorted order:\n", np.sort(arr, axis=None))
