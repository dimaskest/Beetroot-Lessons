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
        if self.isEmpty() or item not in self.items:
            raise ValueError("Either stack is empty or there is no such element in it")
        
        if self.peek() == item:
            return self.pop()
        else:
            t_list = []
            while self.peek() != item:
                t_list.append(self.pop())
            
            res = self.pop()
            while t_list:
                self.push(t_list.pop())
            
            return res

    def __repr__(self) -> str:
        return f"Stack - {self.items}"

# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.get_from_stack(20))
# print(stack)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def get_from_queue(self, item):
        if self.isEmpty() or item not in self.items:
            raise ValueError("Either queue is empty or there is no such element in it")
        
        self.items.remove(item)

    def __repr__(self) -> str:
        return f"Q - {self.items}"

# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.get_from_queue(20)
# print(q)

# Зробив двома способами. По суті зі стеком можна було б теж в одну стрічку, 
# і це було б логічніше, мені здається, але наврядчи ж завдання таке просте :D
# + не дуже розумію, навіщо повертати елемент (так в завданні), якщо ми вказуємо, який видаляти
