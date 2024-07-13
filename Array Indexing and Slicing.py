import numpy as np

array_4x4 = np.arange(1, 17).reshape(4, 4)
print("Original 4x4 array:")
print(array_4x4)

sub_array = array_4x4[2:, 2:]
print("\nSub-array (last two rows and columns):")
print(sub_array)
