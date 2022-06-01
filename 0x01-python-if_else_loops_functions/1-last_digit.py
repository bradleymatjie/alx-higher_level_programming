#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)

lastd = int(str(number)[-1])

if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif lastd == 0:
    print(f"Last digit of {number} is {lastd} and is 0")
elif lastd < 6 and lastd != 0:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
