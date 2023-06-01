
# Given a tree Node class, 
# write a method that returns the number of nodes in the tree. (self is the root of the tree).

class Node:
  """Node in a tree."""
  def __init__(self, data, children=None):
      self.data = data
      self.children = children or []
      
  def count_nodes(self):
      
      count = 0
      to_visit = [self]
      
      while to_visit:
          count += 1
          current_node = to_visit.pop() #DFS
          to_visit.extend(current_node.children)
          
      return count

  
new_node1 =Node(1)
new_node2 =Node(2)
new_node3 =Node(3)
new_node4 =Node(4)
new_node5 = Node(5)

new_node_tree = Node(new_node1, [Node(new_node2, [new_node5, new_node3]), new_node3, new_node4])

print(new_node_tree.count_nodes())