import numpy as np

def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        x = float(s)
        if x%1 == 0:
            print("This number is an integer.")
        if x%1 != 0:
            print("This number is not an integer.")
    except ValueError:
        print("This is not a number")


x = input("Enter a string:\n")
print("Is this a an integer?")
print(is_number_tryexcept(x))

