# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

x = 0
y = 1
z = x + y
sum = 0

while (x + y < 4000000):
    z = x + y
    x = y
    y = z
    if z % 2 == 0:
        sum += z

print(sum)