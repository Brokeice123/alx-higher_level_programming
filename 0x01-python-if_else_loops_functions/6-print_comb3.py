#!/usr/bin/python3
for digit in range(0, 8):
    for digit2 in range(digit + 1, 10):
        print("{:d}{:d}".format(digit, digit2), end=", ")
print("{:d}{:d}".format(digit + 1, digit2))
