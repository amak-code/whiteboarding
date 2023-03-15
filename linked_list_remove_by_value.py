# Write a function that removes a node with a given value 
# from a singly-linked list. It should return the head node. 
# The function should take in two arguments:
# head — the head of a linked list
# value — a value that you want to remove

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
	

def remove_by_value(head, value):
    
    if head.data == value:
        head = head.next
        return head.data
    
    curr_node = head

    while curr_node.next:

            if curr_node.next.data == value:
                curr_node.next = curr_node.next.next
                break
            curr_node = curr_node.next
   

    return head.data



new_node1 =Node(1)
new_node2 =Node(2)
new_node3 =Node(3)
new_node4 =Node(4)
new_node5 = Node(5)

new_node1.next = new_node2
new_node2.next = new_node3
new_node3.next = new_node4
new_node4.next = new_node5

print(remove_by_value(new_node1, 1))