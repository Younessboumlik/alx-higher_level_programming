#!/usr/bin/python3
import random
s = 1
number = random.randint(-10000, 10000)
if number < 0:
    s = -1
i = s * str(number)[-1]
if (s * int(str(number)[-1]) > 5):
    print("Last digit of", number, "is", i, "and is greater than 5")
elif (s * int(str(number)[-1]) == 0):
    print("Last digit of", number, "is", i, "and is 0")
else:
    
    print("Last digit of", number, "is", i, "and is less than 6 and not 0")
