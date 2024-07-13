import numpy as np

array_1d = np.arange(1, 13)
reshaped_array = array_1d.reshape(3, 4)
transposed_array = reshaped_array.T

print("Reshaped array (3x4):")
print(reshaped_array)
print("\nTransposed array (4x3):")
print(transposed_array)
