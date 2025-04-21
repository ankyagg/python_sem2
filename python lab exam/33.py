def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

def nCr(n,r):
    if r>n:
        return 0
    else:
        return factorial(n)/(factorial(r)*factorial(n-r))


n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))


print(f"{n}C{r} = {nCr(n, r)}")
