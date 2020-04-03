# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
# words, how many letters would be used?

values = {
    1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 
    10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 
    20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6,100:7, 
    1000:11, "and":3
    }

def get_length(x):
    # Because we want value of 'one-hundred' and not just 'hundred' when x == 100
    if x in values and not x == 100:
        return values[x]

    length = 0

    if x>20 and x<100:
        units = x%10
        tens = x - units
        length = values[tens] + values[units]
    # For multiples of 100

    elif not x%100:
        hundreds = int(str(x)[:1])
        length = values[hundreds] + values[100]

    elif x>100 and x<1000:
        hundreds = int(str(x)[:1])
        tens_and_units = x % 100
        length = values[hundreds] + values[100] + values["and"] + get_length(tens_and_units)

    return length

# sum of length of numbers one to one-thousand written in words
answer = 0
for i in range(1, 1001):
    answer += get_length(i)
print("The sum is %d." %(answer))
