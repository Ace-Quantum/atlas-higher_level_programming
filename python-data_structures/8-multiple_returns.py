#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a < 0:
        b = None
    else:
        b = sentence[0]
    result = (a, b)
    return result

