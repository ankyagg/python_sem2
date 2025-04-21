# Get marks/percentage from user
percentage = float(input("Enter your percentage: "))

# Using if-elif-else ladder
if percentage < 35:
    print("Result: Fail")
elif percentage < 50:
    print("Result: Pass")
elif percentage < 60:
    print("Result: Second Class")
elif percentage < 75:
    print("Result: First Class")
else:
    print("Result: Distinction")
