# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

def find_abc(s):
    for a in range(1, s):
        for b in range(1, a):
            c = s-a-b
            if c**2 == a**2 + b**2:
                return a*b*c

print(find_abc(1000))
