# Find the sum of all the primes below two million.

limit = 2000000

sum = 0
non_primes = set() # set of all non prime numbers
for i in range(2, limit):
    # Add to sum if prime
    if i not in non_primes:
        sum += i
    # Add all multiples of i below limit to non_primes
    non_primes.update(range(i*2, limit, i))

print("The sum of all the primes below 2 million is %d" % sum)