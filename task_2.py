class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def isempty(self):
        return self.head == None
    
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.isempty():
            return None
        else:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.data
    
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while iternode != None:
                print(iternode.data, end = "")
                iternode = iternode.next
                if iternode != None:
                    print(" -> ", end = "")
            return

stack = Stack()