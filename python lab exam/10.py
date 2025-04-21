a = int(input("Enter the first no. :"))
b = int(input("Enter the second no.: "))

try:
    division = (a/b)
    print(division)
except ZeroDivisionError:
    print("You are trying to divide by a zero, Try another non-zero value")
