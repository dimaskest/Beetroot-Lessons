class RangeNew:
    def __init__(self, i, to_i, step):
        self.i = i
        self.to_i = to_i
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i > self.to_i:
            raise StopIteration
        val = self.i
        self.i += self.step
        return val

list_ = [10, 20, 30, 50, 60, 70, 80, "a", "b"]

# Range_new + enumerate :D
for i in RangeNew(0, len(list_) - 1, 1):
    print(i, list_[i])