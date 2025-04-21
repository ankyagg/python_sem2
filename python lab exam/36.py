import re

def validate_phone(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern,mobile)

def validate_email(email):
    pattern = r'^[\w._-]+@[a-z]+\.\w{2,}$'
    return re.match(pattern,email)

mobile = input("Enter your Moile no.: ")
email = input("Enter your Email ID: ")

if validate_phone(mobile):
    print("Mobile no. is valid")

else:
    print("Invalid, please put 10 digits.")

if validate_email(email):
    print("Email ID is valid")

else:
    print("Invalid")
    
