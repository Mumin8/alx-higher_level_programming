#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """delete at an index"""

    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_liist
    del my_list[idx]
    return my_list
