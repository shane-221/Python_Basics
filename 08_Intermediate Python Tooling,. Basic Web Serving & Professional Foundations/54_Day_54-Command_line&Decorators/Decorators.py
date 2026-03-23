import time 



#### Delay decorator  -----------------------------------------------------####
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


### Decorator function being applied 
@delay_decorator
def say_hello():
    print("Hello")