# What is the value of the first triangle number to have over five hundred divisors?

from itertools import chain

i = 1 # index

while (True):
    # triangle number of i-index using formula
    num = i * (i + 1) // 2
    
    # all divisors of num
    divisors = set( 
        chain.from_iterable( 
            [j, num // j] for j in range(1, int(num**0.5)+1) if not num % j 
            ) 
        )

    # if divisors are more than 500, we have our answer
    if (len(divisors)> 500):
        print("The first triangle number to have over 500 divisors is %d." % num)
        break

    i += 1
