class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 



class Linkedlist(Node):
    def __init__(self):
        self.head = None 
    
    def display(self):
        current = self.head
        if current is None:
            print('EMPTY')
        else:
            while current is not None:
                print(current.data)
                current = current.next
    def insert(self, data):
        current = self.head
        if  current is None:
            self.head = Node(data)
        else:
            while current.next is not None:
                 current = current.next
            current.next = Node(data)
            
list = Linkedlist()
list.insert('test   1')
list.insert('test   2')
list.insert('test   3')
list.insert('test   4')

list.display()
