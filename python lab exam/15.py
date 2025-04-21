import numpy as np

arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],[3,4,5]])
arr_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

reshape_1dto2d = arr_1d.reshape(5,1)
print(reshape_1dto2d)

print("\nSlicing 1D Array (First three elements):")
print(arr_2d[0:])
