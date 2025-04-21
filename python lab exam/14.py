import re

def validate_pass(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern,password):
        return True
    else:
        return False

password =  input("Enter your password: ")

if validate_pass(password):
    print("Valid Password")

else:
    print("Invalid password")


#pattern = '^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[$@#%&!])[A-Za-z\d@$%!#]{8,}$'
