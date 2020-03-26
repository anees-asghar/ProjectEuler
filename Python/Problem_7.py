# What is the 10 001st prime number?

# test if x is prime
def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

counter = 0 # prime counter
i = 1 # iterator

while(counter < 10001):
    i += 1
    if isPrime(i):
        counter += 1

print("The 10001th prime number is %d." % (i))