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

