class Binary_Search_Tree:

  class __BST_Node:

    # def __init__(self, value):
    # Initializes the private attributes of the binary search tree
    def __init__(self, value):
      self.value = value
      self.right__child = None
      self.left__child  = None
      self.height = 0

  # def __init__(self):
  # Initializes the root of the binary search tree to None
  def __init__(self):
    self.__root = None

  # def insert_element(self, value):
  # Checks to see if the root has nothing in it
  # If so, it inserts at the root of the tree
  # Otherwise it inserts the value in the tree
  # using the private recursive function _insert,
  # incrementing the height when completed
  def insert_element(self, value):

    if (self.__root == None):
      self.__root=self.__root.__BST_Node(value)
      self.__root.height = self._height(self.__root)
    
    else:
      self._insert(value, self.__root)
      self.__root.height = self._height(self.__root)
  
  # def _insert(self, value, current_node):
  # Private method for insertion method
  # Checks to see if the value is less than or greater than the current node
  # If it is less, it goes to the left child,
  # if it is greater it goes to the right child
  # It then checks to see if the nodes are none, and places if yes, otherwise
  # returns the inserted value in the child, or raises a value error if
  # not able to insert
  def _insert(self, value, current_node):
    if (value < current_node.value):
      if (current_node.left__child == None):
        current_node.left__child=current_node.left__child.__BST_Node(value)
      else:
        return self._insert(value, current_node.left__child)

    elif (value > current_node.value):
      if(current_node.right__child == None):
        current_node.right__child=current_node.right__child.__BST_Node(value)
      else:
        return self._insert(value, current_node.right__child)
    
    else:
      raise ValueError  

  # def remove_element(self, value):
  # Sets the root to the private recursive function _remove
  # Updates the height after the removal
  def remove_element(self, value):
    self.__root = self._remove(self.__root, value)

    if (self.__root):
      self.__root.height = self._height(self.__root)
  
  # def _remove(self, current_node, value):
  # Private removal method for removing element
  # Checks to see if the values of the tree
  # If non exists it raises a value error, otherwise
  # checks if it is greater or less, and goes to the right or left side
  # It also checks if it is the root node and sees if it has either/or
  # right and left children and removes the values accordingly
  # additionally it uses the left0most value to replace node as we
  # have done in class.
  def _remove(self, current_node, value):
    if (current_node == None):
      raise ValueError
    
    elif (value > current_node.value):
      current_node.right__child = self._remove(current_node.right__child, value)
  
    elif (value < current_node.value):
      current_node.left__child = self._remove(current_node.left__child, value)
  
    elif (value == current_node.value):
      if(current_node.right__child == None):
        current_node = current_node.left__child
  
      elif (current_node.left__child == None):
        current_node = current_node.right__child
  
      else:
        right_child = current_node.right__child
        while (right_child.left__child):
          right_child = right_child.left__child
        current_node.value = right_child.value
        current_node.right__child = self._remove(current_node.right, right_child.value)

  # def in_order(self):
  # Returns the private recursive function _in_order
  def in_order(self):
    return self._in_order()

  # def _in_order(self):
  # Private recursive method for in-order
  # Checks to see if there is no value in root, then returns
  # [ ] as a result, otherwise recursively strings the 
  # nodes with the in-order format and returns the result for display
  def _in_order(self):
    if (self.__root == None):
      return "[ ]"

    else:
      string_in_order = "[ "
      string_in_order = self._print_in_order(self.__root, string_in_order)
      string_in_order = string_in_order[0:-2] + " ]"
      return string_in_order
  
  # def _print_in_order(self, current_node, string_in_order):
  # Private recursive print method for in-order
  # Checks the right children first, then left children, strings the result
  # and returns it.
  def _print_in_order(self, current_node, string_in_order):
    if (current_node.right__child != None):
      string_in_order = self._print_in_order(current_node.right__child, string_in_order)
    
    if (current_node.left__child == None):
      string_in_order = string_in_order + str(current_node.value) + ", "
  
    else:
      string_in_order = string_in_order(current_node.left__child, string_in_order)
      string_in_order = string_in_order(current_node.value) + ", "
    return string_in_order

  # def pre_order(self):
  # returns the private recursive function _pre_order
  def pre_order(self):
    return self._pre_order()

# def _pre_order(self):
# Private recursive method for pre-order
# Checks if root is empty and returns [ ]
# Oherwise it calls the private recursive string function
# to string the nodes in pre-order
# it then returns the final result
  def _pre_order(self):
    if (self.__root == None):
      return "[ ]"
    
    else:
      string_pre_order = "[ "
      string_pre_order = self._print_pre_order(self.__root, string_pre_order)
      string_pre_order = string_pre_order[0:-2] + " ]"
      return string_pre_order

# def _print_pre_order(self, current_node, string_pre_order):
# Private stringing recursive method for pre-order
# Begins by putting the string variable to itself and the node value added by a 
# comma. It then goes to the left child followed by right child and
# returns the string result
  def _print_pre_order(self, current_node, string_pre_order):
    string_pre_order = string_pre_order + str(current_node.value) + ", "

    if(current_node.left__child != None):
      string_pre_order = self._print_pre_order(current_node.left__child, string_pre_order)

    if(current_node.right__child != None):
      string_pre_order = self._print_pre_order(current_node.right__child, string_pre_order)
    return string_pre_order

  # def post_order(self):
  # Returns the private recursive method _post_order
  def post_order(self):
    return self._post_order()

# def _post_order(self):
# Private recursive method for post-order
# Checks if the root is empty and returns [ ]
# Otherwise it initiates a string variable and calls
# the private string recursive method for the post-order
# and returns the result
  def _post_order(self):
    if (self.__root == None):
      return "[ ]"
    
    else:
      string_post_order = "[ "
      string_post_order = self._print_post_order(self.__root, string_post_order)
      string_post_order = string_post_order[0:-2] + " ]"
      return string_post_order

# def _print_post_order(self, current_node, string_post_order):
# Private string recursive method for the post-order
# Goes through the left children first stringing together the values
# Then it goes through the right children and returns the final result
  def _print_post_order(self, current_node, string_post_order):
    if (current_node.left__child != None):
      string_post_order = self._print_post_order(current_node.left__child, string_post_order)

    if (current_node.right__child == None):
      string_post_order = string_post_order + str(current_node.value) + ", "

    else:
      string_post_order = self._print_post_order(current_node.right__child, string_post_order)
      string_post_order = string_post_order + str(current_node.value) + ", "
    return string_post_order

  # def get_height(self):
  # Returns the height of the tree
  def get_height(self):
    if (self.__root != None):
      return self.__root.height

    else:
      return 0

# def _height(self, current_node):
# Private method for the height
# Checks the left child first then returns the max height
# Checks the right child and returns the max height
# Or if there are both left and right, checks them both and
# returns the max value. It always adds 1 because of the root
# otherwise if it has neither just returns 1
  def _height(self, current_node):
    if (current_node.left__child):
      return 1 + max(self._height(current_node.left__child)) 
     
    elif (current_node.right__child):
      return 1 + max(self._height(current_node.right__child))

    elif (current_node.left__child & current_node.right__child):
      return 1 + max(self._height(current_node.left__child),self._height(current_node.right__child))

    else:
      return 1
      
  # def __str__(self):
  # Returns the default string method used of in-order format
  def __str__(self):
    return self.in_order()

# if __name__ == '__main__':
#  pass #unit tests make the main section unnecessary.

