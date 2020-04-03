# Evaluate the sum of all the amicable numbers under 10000.

from itertools import chain

def sum_of_factors(x):
    # Sum of all the factors of a numbers excluding the number itself
    factors = set(chain.from_iterable([i, x/i] for i in range(2,int(x**0.5)+1) if not x%i))
    return int(sum(factors) + 1)

# Generating sum of factors for all numbers i below 10001
values = {i:sum_of_factors(i) for i in range(1, 10001)}

# Storing amicables
amicables = set()

# Finding amicables
for i in values:
    if values[i] in values:
        if values[values[i]] == i and not i == values[i]:
            amicables.update([i, values[i]])

# Output
print( "The sum is %d." % (sum(amicables)) )