def test():
    def square(a: int):
        return a**2
    return square

func = test()
print(func(5))