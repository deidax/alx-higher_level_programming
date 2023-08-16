#!/usr/bin/python3
import random


number = random.randint(-10, 10)
s = "{:d} is positive".format(number) if number > 0 else ("{:d} is negative".format(number) if number < 0 else "is zero")
print(s)
