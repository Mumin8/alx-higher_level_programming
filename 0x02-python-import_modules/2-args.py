#!/usr/bin/python3
if __name__ == "__main__":
    """this function prints arguments"""
    import sys
    
    if len(sys.argv) - 1 == 0:
        print("0 argument.")
    elif len(sys.argv) - 1 == 1:
        print("1 argument:")
    else:
         print("{} arguments:".format(len(sys.argv) - 1))
    for ind, arg in enumerate(sys.argv):
             if ind >= 1:
                 print("{}: {}".format(ind, arg))

