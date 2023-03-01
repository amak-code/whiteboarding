# Define a Queue class and implement the following methods: __init__, enqueue, 
# dequeue, and is_empty. Specify the runtime of all methods except __init__.

# Bonus: How can we implement the queue so that all three runtimes are O(1)?

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, value = None):
            self.value = value
            self.next = None


    def __repr__(self):
        if not self.head:
            return "<Queue (empty)>"
        else:
            return f"<Queue head={self.head.value} tail={self.tail.value}>"

    def enqueue(self, value):
        new_node = self.Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return
        self.head = self.head.next


    def is_empty(self):
        return self.head == None


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)


q.dequeue()
q.dequeue()


print(q)