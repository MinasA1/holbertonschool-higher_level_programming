#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number % -10
else:
    num = number % 10 
if num > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, num))
elif num == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, num))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, num))
