#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """reurns a tuple """

    length = len(sentence)
    if length == 0:
        tup = (None, 0)
    else:
        tup = (length, sentence[0])
    return tup
