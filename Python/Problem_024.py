# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

# All permutations of the given digits, sorted
perms = sorted( set( "".join(i) for i in permutations("0123456789") ) )

# Output
print("The millionth permutation is %s." % (perms[999999]))