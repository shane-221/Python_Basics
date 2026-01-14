#Todo: Args for positional arguments
def add(*args):
    print(args[1])

    x=0
    for n in args:
      x+=n
    return x

print(add(3,5,7,9))


# Todo: Creation of unlimited keyword arguments.
def calculate(n=None, **kwargs):
    print( kwargs)

    # Can also split them into their key valur pairs
    for (key, value) in kwargs.items():
        print(key)
        print(value)

    # Can also do it this way:
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate( 2, add =3 , multiply = 4)