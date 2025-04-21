import numpy as np

array1 = np.array([[10,20,6],[5,8,3]])
array2 = np.array([[30,40,5],[9,7,1]])

addition = array1+array2

multiplication = array1*array2

subtraction = array1-array2

division = np.round((array1/array2),2)

print(f"Addition: \n{addition}")
print(f"Multiplication: \n{multiplication}")
print(f"Subtraction: \n{subtraction}")
print(f"Division: \n{division}")
