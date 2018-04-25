# File: Non-limit_amount_of-arguments_in_Functions_in_Python.py
# Description: Non-limit amount of arguments in Functions in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Non-limit amount of arguments in Functions in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Non-limit_amount_of-arguments_in_Functions_in_Python (date of access: XX.XX.XXXX)


# Non-limit amount of arguments in the function
def printab(a, b, *args):
    print('positional argumnet a', a)
    print('positional argument b', b)
    print('additional argument(s):')
    for arg in args:
        print(arg)
    print(type(args))  # This is a tuple

printab(10, 20, 30, 40, 50)

def printab(a, b, **kwargs):
    print('positional argumnet a', a)
    print('positional argument b', b)
    print('additional argument(s):')
    for key in kwargs:
        print(key, kwargs[key])
    print(type(kwargs))  # This is a dictionary

printab(10, 20, c=30, d=40, jimi=50)

