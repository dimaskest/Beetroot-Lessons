

def arg_rules(type_: type, max_length: int, contains: list):
    def function(func):
        def wrapper(name):
            sentence = func(name)
            if type(name) != str:
                print("Type of entered data is not str")
                return False
            if len(name) > 15:
                print("Lenght of entered name is > 15")
                return False
            if name in contains:
                print("Entered data contains forbidden symbol or combination of them")
                return False
            return sentence
        return wrapper
    return function


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

print(create_slogan("S@SH05"))