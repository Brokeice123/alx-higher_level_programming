#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
        second = None
    else:
        first = sentence[0]
        second = sentence[1:]
    return length, first, second
