# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

import os

# # Opening, reading and cleaning file
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
Ofile = open(os.path.join(__location__, 'Files/names.txt'))
RFile = Ofile.read().replace('"', '').split(',')
names = sorted(RFile)

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to calculate name score
def name_score(name):
    score = 0
    for char in name:
        score += (Alphabet.index(char) + 1)
    index = names.index(name) + 1
    score *= index
    return score

# Adding up the scores
total = 0
for name in names:
    total += name_score(name)

# Output
print("The total of all name scores is %d." % (total))