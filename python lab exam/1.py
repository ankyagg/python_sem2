import numpy as np

BS= float(input("Enter your gross salary"))

DA = 0.7*BS

HRA = 0.1*BS

TA = 0.3*BS

Gross_salary = BS + DA + HRA + TA
np.round(Gross_salary,3)
print(f"Your gross salary is {Gross_salary}")

#importing numpy so that i can use round function from its library
