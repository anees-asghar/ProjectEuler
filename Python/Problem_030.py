# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Function to check if x meets our requirements
def does_x_satisfy(x):
    special_sum = sum( [ int(i)**power for i in str(x) ] )
    if x == special_sum:
        return True
    return False

# Finding the upper limit: We want to find n, such that n*9**5 gives us an n digit number. This can be done
# by taking 5 or 6 as n. 6 * 9**5 = 354294 and that is our upper limit
upper_limit = 354294

# Input
power = 5

# Adding all numbers that satisfy the equation
answer = 0
for i in range(2, upper_limit):
    if does_x_satisfy(i):
        answer += i

# Output
print("The sum is %d." % (answer))