import numpy as np

# -------------------------------
# 1D Array
# -------------------------------
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr_1d)

# Reshape 1D to 2D (1 row, 5 cols)
reshaped_1d = arr_1d.reshape(5,1)
print("Reshaped 1D to 2D:\n", reshaped_1d)

# Slice 1D (get elements 1 to 3)
slice_1d = arr_1d[1:4]
print("Sliced 1D [1:4]:", slice_1d)

# Index 1D
print("Index arr_1d[2]:", arr_1d[2])

# -------------------------------
# 2D Array
# -------------------------------
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr_2d)

# Reshape 2D to (3, 2)
reshaped_2d = arr_2d.reshape(3, 2)
print("Reshaped 2D to (3,2):\n", reshaped_2d)

slice_2d = arr_2d[:2, 0]
print("Sliced 2D (rows 0-1, column 0):", slice_2d)

# Index 2D
print("Index arr_2d[1][2]:", arr_2d[1][2])

# -------------------------------
# 3D Array
# -------------------------------
arr_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:\n", arr_3d)

# Reshape 3D to (4,2)
reshaped_3d = arr_3d.reshape(4, 2)
print("Reshaped 3D to (4,2):\n", reshaped_3d)

# Slice 3D (get first block)
slice_3d = arr_3d[0]
print("Sliced 3D block 0:\n", slice_3d)

# Index 3D
print("Index arr_3d[1][1][0]:", arr_3d[1][1][0])
