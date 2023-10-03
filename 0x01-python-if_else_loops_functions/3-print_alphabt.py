#!/usr/bin/python3
for j in range(97, 123):
    if j == 113 or j == 101:
        continue
    print("{:c}".format(j), end='')
