class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def get_from_stack(self, item):
        if isinstance(item, int) and item in range(0, self.size()):
            return self.items[item]
        else:
            if isinstance(item, str):
                raise ValueError("Please use integers only")
            if item > self.size() or item < 0:
                raise KeyError("Stack index out of range or less than 0")


stack = Stack()
stack.push("10")
stack.push(20)
stack.push("apple")
stack.push(True)

print(stack.get_from_stack())