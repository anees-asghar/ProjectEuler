# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
# We know that all integers greater than 28123 can be written as the sum of two abundant numbers.

from itertools import chain

# Function to check if a number is abundant
def isAbundant(x):
    # As we only need proper factors(i.e. not the numbers itself), we check for factors
    # between 1 and the number and later add '1' to the sum
    factors = set(chain.from_iterable([i, x//i] for i in range(2, int(x**0.5)+1) if not x%i))
    if sum(factors) + 1 > x:
        return True
    return False

# Finding all abundants under 28124
abundants = set([i for i in range(1, 28124) if isAbundant(i)])

# Function to check if a number can be return as the sum of two abundant numbers
def isAbundable(x):
    if x < 24:
        return False
    for i in range(12, x):
        if i in abundants and x-i in abundants:
            return True
    return False

# Storing the sum of non-abundant numbers
answer = 0

# Searching for non-abundant numbers
for i in range(28124):
    if not isAbundable(i):
        answer += i

# Output
print( "The sum of all positive integers that are abundant is %d." % (answer) )