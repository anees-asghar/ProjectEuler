# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

sum_of_numbers = 0
sum_of_squares = 0

for i in range(1, 100):
    sum_of_numbers += i
    sum_of_squares += i**2

print("The difference is %d." % ( sum_of_numbers**2 - sum_of_squares ))