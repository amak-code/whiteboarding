class Stack:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, value = None):
            self.value = value
            self.next = None

    
    def pop(self):
        if self.is_empty():
            return
        else:
            temp = self.head
            self.head = self.head.next

            return temp.value


    def push(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node
            
            

    def is_empty(self):
        
        return self.head == None