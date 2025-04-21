n = int(input("Enter to calculate factorial"))

factorial = lambda n : 1 if n==0 or n==1 else n*factorial(n-1)

print(factorial(n))

#using recursion approach
