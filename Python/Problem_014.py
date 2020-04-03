# Which starting number, under one million, produces the longest Collatz chain?


# Storing already stored collatz values for faster access
collatz_values = {1: 1}

def CollatzLength(n):
    if n in collatz_values:
        return collatz_values[n]

    if not n%2:
        # As CollatzLength(a) when a i even is just CollatzLength(a/2)+1
        collatz_values[n] = CollatzLength(n/2) + 1
    else:
        # As CollatzLength(a) when a is odd is just CollatzLength((3*a+1)/2)+2
        collatz_values[n] = CollatzLength((3*n + 1)/2) + 2
    
    return collatz_values[n]


answer = 0
longest_chain_size = 0

# Because CollatzLength(2a) will always be greater than CollatzLength(a), we can start from 500000
for i in range(500000, 1000000):
    chain_size = CollatzLength(i)
    if chain_size > longest_chain_size:
        answer = i
        longest_chain_size = chain_size

print("%d produces the longest Collatz chain." % answer)