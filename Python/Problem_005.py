# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Smallest positive number that is divisible by a range of number is the least common multiple of that range of numbers.

# find lcm of two numbers (x, y)
def lcm(x, y):
    greater = x
    if (y > x):
        greater = y
    while(True):
        if greater % x == 0 and greater % y == 0:
            return greater
            break
        greater += 1

# find the lcm of all numbers within a range (lowerLimit to upperLimit)
def recursive_lcm(lowerLimit, upperLimit):
    if upperLimit == lowerLimit:
        return lowerLimit
    return lcm(recursive_lcm(lowerLimit, upperLimit-1), upperLimit)

# We do not need to check for the 1-10 as if a number is divisible by 11-20, it must also be divisible by 1-10
print(recursive_lcm(11, 20))