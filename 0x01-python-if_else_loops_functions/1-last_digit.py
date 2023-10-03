#!/usr/bin/python3
import random
s = 1
number = random.randint(-10000, 10000)
if number < 0:
    s = -1
if (s * number > 5):
    print("Last digit of",number,"is",str(number)[-1],"and is greater than 5")
elif (s * number == 0):
    print("Last digit of",number,"is",str(number)[-1],"and is 0")
elif (s * number < 6 and s * number != 0):
    print("Last digit of",number,"is",str(number)[-1],"and is less than 6 and not 0")
