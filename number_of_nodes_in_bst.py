# Given a BinarySearchNode class, 
# write a method that returns the total number of nodes in the tree.

class BinarySearchNode:
  """Binary tree node."""

  def __init__(self, data, left=None, right=None):
      self.data = data

      self.left = left
      self.right = right


  def __repr__(self):
        """Debugging-friendly representation."""

        return f"<BinaryNode {self.data}>"


  def num_of_nodes_in_bst(self):

        counter = 0
        to_visit = [self]

        while to_visit:
            current = to_visit.pop()
            counter += 1
            if current.left is not None:
                to_visit.append(current.left)
            if current.right is not None:
                to_visit.append(current.right)
        
        return counter

# recuirsive solution

  def num_of_nodes_in_bst_recursively(self):

    if self.left is None:
        left_total = 0
    else:
        left_total = self.left.num_of_nodes_in_bst_recursively()

    if self.right is None:
        right_total = 0
    else:
        right_total = self.right.num_of_nodes_in_bst_recursively()


    return 1 + left_total + right_total



apple = BinarySearchNode("apple")
ghost = BinarySearchNode("ghost")
fence = BinarySearchNode("fence", apple, ghost)
just = BinarySearchNode("just")
jackal = BinarySearchNode("jackal", fence, just)
zebra = BinarySearchNode("zebra")
pencil = BinarySearchNode("pencil", None, zebra)
mystic = BinarySearchNode("mystic")
nerd = BinarySearchNode("nerd", mystic, pencil)
money = BinarySearchNode("money", jackal, nerd)


print(apple.num_of_nodes_in_bst())

print(money.num_of_nodes_in_bst_recursively())