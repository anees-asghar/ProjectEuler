def primes_under(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isPrime) in enumerate(a):
        if isPrime:
            yield i
            for j in range(i*i, limit, i):
                a[j] = False

count = 0
for x in primes_under(1000000):
    count += 1
    
print(count)
