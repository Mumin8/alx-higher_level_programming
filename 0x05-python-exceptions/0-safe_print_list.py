#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    num_elem = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_elem += 1
        except IndexError:
            print
    print()
    return num_elem