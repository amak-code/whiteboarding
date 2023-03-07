# Given a tree Node class, write a method that takes an item as its only parameter and 
# returns True if the data for any node in the tree matches the given item. 
# Otherwise, it should return False.

class Node:
  """Node in a tree."""
  def __init__(self, data, children=None):
        self.data = data
        self.children = children or []


  def find_an_item_in_tree(self, item):

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == item:
                return True
            to_visit.extend(current.children)

        return False


morgan = Node("Morgan",[Node("Rachna", [Node("Masha", [])]),Node("Taylor", [])])


print(morgan.find_an_item_in_tree("Masha"))