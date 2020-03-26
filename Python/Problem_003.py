# What is the largest prime factor of the number 600851475143?

number = 600851475143
factor = 2

while number > factor:
    if number % factor == 0:
        number = number / factor
        factor = 2
    else:
        factor += 1
        
print("The largest prime factor of the number 600851475143 is %d." % (factor))



