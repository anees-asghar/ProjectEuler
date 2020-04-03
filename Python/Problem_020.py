# Find the sum of the digits in the number 100!

# Factorial function
def factorial(x):
    if x==1:
        return 1
    return factorial(x-1) * x

# Adding the digits in 100!
answer = sum( [int(i) for i in str(factorial(100))] )

# Output
print("Sum is %d." % ( answer ))