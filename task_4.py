class CustomException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

        with open("logs.txt", "a+") as file:
            file.write(self.msg + "\n")


def make_division(n):
    try:
        return n / 2
    except TypeError:
        error_message = f"{n} is a wrong value"
        raise CustomException(error_message)


print(make_division("word"))