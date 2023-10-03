#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (abs(number) > 5):
    print("Last digit of",number,"is",str(number)[-1],"and is greater than 5")
elif (abs(number) == 0):
    print("Last digit of",number,"is",str(number)[-1],"and is 0")
elif (abs(number) < 6 and abs(number) != 0):
    print("Last digit of",number,"is",str(number)[-1],"and is less than 6 and not 0")
