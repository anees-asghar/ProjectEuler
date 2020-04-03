# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


# As we have to move east and south 20 times each, we can calculate how many possible 40 step combinations of 20-Es (east) and 20-Ss (south)
# are there. So, we can use the formula to find combinations, 40 choose 20, which is 40! / ((40-20)!*20!)

# Storing values for quicker access
values = {1:1}

# Calculate factorial
def factorial(x):
    if x in values:
        return values[x]
    values[x] =  x * factorial(x-1)
    return values[x]

def possible_routes(grid_size):
    # Formula to find number of possible routes
    answer = factorial(grid_size*2) / (factorial(grid_size) * factorial(grid_size))
    return int(answer)

print( "There are %d possible routes." % (possible_routes(20)) )