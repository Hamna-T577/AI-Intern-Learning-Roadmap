def logger(func):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = func(*args, **kwargs)

        print("Function Finished")

        return result

    return wrapper