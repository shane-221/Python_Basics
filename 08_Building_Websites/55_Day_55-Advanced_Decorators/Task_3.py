## Args and Kwargs in Decorators

# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper_function(*args):
        name = function.__name__
        result = function(*args)
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {result}")
        return result

    return wrapper_function


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)