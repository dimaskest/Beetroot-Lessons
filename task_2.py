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

for i in RangeNew(0, 50, 10):
    print(i)