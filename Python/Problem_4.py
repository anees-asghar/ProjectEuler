# Find the largest palindrome made from the product of two 3-digit numbers.

lpn = 0

for i in range(0, 999):
    for j in range(0, 999):
        k = i * j
        kStr = str(k)
        if kStr == kStr[::-1] and k > lpn:
            lpn = k

print("The largest palindrome made from the product of two 3-digit numbers is %d" % (lpn))
