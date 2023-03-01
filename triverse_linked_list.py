# Part 1: Define a class for a linked list node.

# Part 2: Write a function that takes in the head node of a linked list
# and prints the data of every node in the list.

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
	
def print_data(head_node):
  
    node = head_node

    while node is not None:
            print(node.data)
            node = node.next

new_node1 =Node(1)
new_node2 =Node(2)
new_node3 =Node(3)
new_node4 =Node(4)
new_node5 = Node(5)

new_node1.next = new_node2
new_node2.next = new_node3
new_node3.next = new_node4
new_node4.next = new_node5

print_data(new_node1)