# Take a single character input from the user
char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
elif char.isdigit():
    print("It's a digit.")
elif char.islower():
    print("It's a lowercase letter.")
elif char.isupper():
    print("It's an uppercase letter.")
else:
    print("It's a special character.")
