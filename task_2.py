class Mathematician:
    def __init__(self) -> None:
        pass
    
    def square_nums(self, list_: list):
        return [num ** 2 for num in list_]
    
    def remove_positives(self, list_: list):
        return [num for num in list_ if num < 0]
    
    def filter_leaps(self, list_: list):
        return [year for year in list_ if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0))]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]