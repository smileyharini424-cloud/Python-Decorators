def decorator(function):
    def wrapper():
        print("Before function execution")

        function()

        print("After function execution")

    return wrapper


@decorator
def greet():
    print("Hello, Harini!")


greet()
