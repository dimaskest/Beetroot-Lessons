class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    # def __repr__(self) -> str:
    #     return f"Node({self.data},{self.next})"
    

class UnorderedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        self.size += 1

    def index(self, data):
        if self.is_empty():
            print("list is empty")
            return
        
        if self.head.data == data:
            return 1
        
        last_node = self.head
        index = 1
        while last_node.data != data and last_node.next.next != None:
            last_node = last_node.next
            index += 1

        if last_node.next.data == data:
            return index + 1
        else:
            print("there is no such element in a list")
            return
    
    def pop(self):
        if self.head is None:
            return

        last_node = self.head
        counter = 1
        while counter != (self.size - 1):
            last_node = last_node.next
            counter += 1
        
        last_node.next = None
        self.size -= 1

    def insert(self, index, data):        
        if index < 0 or self.is_empty():
            print("list index is out of range")
            return
        
        if index == self.size or index > self.size:
            self.append(data)
            return

        if index == 1:
            self.push(data)
            return
        
        new_node = Node(data)
        index_node = self.head
        index_counter = 1
        while index_counter != index - 1:
            index_node = index_node.next
            index_counter += 1

        new_node.next = index_node.next
        index_node.next = new_node
        self.size += 1

    def slice(self, start, stop):
        if self.is_empty():
            print("list is empty")
            return
        
        last_node = self.head
        while last_node.data != start:
            last_node = last_node.next

        while last_node.data != stop:
            print(last_node.data, "-> ", end = "")
            last_node = last_node.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
     
    def display(self):
        iternode = self.head
        if self.is_empty():
            print("List is empty")
        else:
            while iternode != None:
                print(iternode.data, end = "")
                iternode = iternode.next
                if iternode != None:
                    print(" -> ", end = "")
            return

l = UnorderedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(60)
l.append(70)
l.append(80)
l.append(90)

l.slice(0, 10)