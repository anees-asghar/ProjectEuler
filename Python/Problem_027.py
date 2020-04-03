# Considering quadratics of the form: n2+an+b, where |a|<1000 and |b|≤1000
# Find the product of the coefficients, a and b, for the quadratic expression that produces 
# the maximum number of primes for consecutive values of n, starting with n=0.

# Function to check if a number is prime
def isPrime(x):
    x = abs(x)
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if not x%i:
            return False
    return True

# Function to find number of consecutive primes using a and b in the quadratic equation
def NOP(a, b):
    n = 0
    while True:
        x = n**2 + a*n + b
        if not isPrime(x):
            break
        n += 1
    return n

# As n starts from 0, that means when n = 0, quadratic equation would just become b, so,
# b has to be prime. We find all the possible values < |1000| that b can assume using Sieve 
# of Eratosthenes
def eratosthenes(limit):
    a = [True] * limit
    a[0] = a[1] = False
    primes = []
    for (i, isPrime) in enumerate(a):
        if isPrime:
            primes.append(i)
            for j in range(i*i, limit, i):
                a[j] = False
    return primes

# Values for b
bs = eratosthenes(1000)
bs = bs + (bs*-1)

# Storing our answer - coefficient of a and b that produce most consecutive primes
coeff_prod = 0
# The value for most consecutive number of primes
max_nop = 0

# Looping between our limits
for a in range(-999, 1000):
    for b in bs:
        x = NOP(a, b)
        if x > max_nop:
            max_nop = x
            coeff_prod = a*b

# Output
print( "The product of a and b is %d." % (coeff_prod) )
