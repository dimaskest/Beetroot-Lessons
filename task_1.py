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

list_ = ["10", 20, "grey", True]

def get_reversed_stack(list):
    stack = Stack()
    
    for char in list_:
        stack.push(char)
    
    while stack.size():
        print(stack.pop())

get_reversed_stack(list_)