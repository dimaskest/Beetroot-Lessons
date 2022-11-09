class TypeDecorators:
    
    def to_int(func):
        def wrapper(string):
            if string.isdigit():
                return int(string)
            else:
                raise Exception("Given string can't be converted to int")
        return wrapper
    
    def to_bool(func):
        def wrapper(string):
            if string == "True" or string == "False":
                return bool(string)
            else:
                raise Exception("Given string can't be converted to bool")
        return wrapper
    
    def to_str(func):
        def wrapper(string):
            return f"'{str(string)}'"
        return wrapper
    
    def to_float(func):
        def wrapper(string):
            if string.isdigit():
                return float(string)
            else:
                raise Exception("Given string can't be converted to float")
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True