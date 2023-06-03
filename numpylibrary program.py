import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Element-wise operations
print("Element-wise addition:")
print(arr1 + arr2)

print("\nElement-wise multiplication:")
print(arr1 * arr2)

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("\nMatrix multiplication:")
print(np.dot(matrix1, matrix2))

# Statistical operations
arr3 = np.array([5, 8, 2, 6, 1, 9, 3, 7, 4])
print("\nMean:", np.mean(arr3))
print("Median:", np.median(arr3))
print("Standard Deviation:", np.std(arr3))
