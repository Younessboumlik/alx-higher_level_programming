#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 5):
    print("Last digit of",number,"is",str(number)[-1],"and is greater than 5\n")
elif (number == 0):
    print("Last digit of",number,"is",str(number)[-1],"and is 0\n")
elif (number < 6 and number != 0):
    print("Last digit of",number,"is",str(number)[-1],"and is less than 6 and not 0\n")
