#!/usr/bin/python3
# 6-raise_exception_msg.py

def raise_exception_msg(message=""):
    """raise exception with argument"""

    try:
        raise NameError(message)
    except NameError:
        raise
