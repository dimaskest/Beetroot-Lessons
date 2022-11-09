list_ = [10, 20, 30, 40, 50, 60]

def enumerate_(iterable, start):
    for i in range(len(iterable)):
        print(start + i, iterable[i])

enumerate_(list_, 1)