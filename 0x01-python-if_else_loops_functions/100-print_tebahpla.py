#!/usr/bin/python3
for j in range(26):
    if j % 2 == 0:
        print("{:c}".format(122 - j), end='')
    else:
        print("{:c}".format(90 - j), end='')
