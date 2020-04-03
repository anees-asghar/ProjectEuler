# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Storing already calculated values
values = {0:0, 1:1, 2:1}

# Fibonacci value of nth term
def Fibonacci(n):
    if n in values:
        return values[n]
    x = Fibonacci(n-1) + Fibonacci(n-2)
    values[n] = x
    return x

answer = 1
while True:
    if len(str(Fibonacci(answer))) >= 1000:
        break
    answer += 1 

# Output
print("The index of the first term in the Fibonacci sequence to contain 1000 digits is %d." % (answer))
