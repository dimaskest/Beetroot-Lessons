def logger(func):
    def wrapper(*args, **kwargs):
        nums = []
        for number in args:
            nums.append(number)
        return f"{func.__name__} called with {nums}"
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(10, 5, 20, 40))
print(square_all(10, 10, 10, 20, 30, 40))