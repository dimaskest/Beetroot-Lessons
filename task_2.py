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

def parenthesesChecker(par_string: str):
    stack = Stack()
    balanced = True
    index = 0
    
    while index < len(par_string) and balanced:
        par = par_string[index]
        if par == "(":
            stack.push(par)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()
        
        index += 1
    
    if not stack.isEmpty():
        balanced = False
    
    return balanced

print(parenthesesChecker("(())()"))