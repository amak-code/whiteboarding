# Given a tree Node class, write a method that returns the number of 
# nodes in the tree.

class Node:
  """Node in a tree."""
  def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

  def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

def num_of_nodes(root):
    counter = 0
    to_visit = [root]
    while to_visit:
        current = to_visit.pop()
        counter += 1
        to_visit.extend(current.children)

    return counter


morgan = Node("Morgan",[Node("Rachna", [Node("Masha", [])]),Node("Taylor", [])])


print(num_of_nodes(morgan))
