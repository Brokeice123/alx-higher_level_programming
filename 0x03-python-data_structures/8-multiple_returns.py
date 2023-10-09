#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        result = (length, sentence[0:1])
        return result
