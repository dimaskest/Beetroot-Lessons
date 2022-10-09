def count_locals(func):
    def wrapper(*args):
        res = func(*args)
        print("There is ", func.__code__.co_nlocals, "local variables in fucntion.")
        return res
    return wrapper

@count_locals
def abc():
    a = 1
    b = 2
    c = 3
    
    return a + b + c
    
abc()