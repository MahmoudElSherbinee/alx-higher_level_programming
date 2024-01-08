#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    letter = sentence[0] if length > 0 else None
    new_tuple = (length, letter)
    return new_tuple
