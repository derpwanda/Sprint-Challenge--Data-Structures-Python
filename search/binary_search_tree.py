class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  #  pre-order fashion?
  def depth_first_for_each(self, cb):
    print(f"self", self)
    stack = []
    print(f"stack after", stack)
    stack.append(self)
    cb(self.value)
    # add to stack with no node/value?
    # FILO, append the stack
    # stack.append(node)
    while len(stack) > 0:
      print(f"while", stack)
      current = stack.pop()
      
      if current.right is not None:
        stack.append(current.right)
        cb(current.right.value)
        #current = current.right
        
      if current.left is not None:
        stack.append(current.left)
        cb(current.left.value)
        #current = current.left


      print(f"stack end while", stack)

    # cb(self.value)
    # if self is None:
    #   return
    # if self.left:
    #   self.depth_first_for_each(cb)   
    # if self.right:
    #   self.depth_first_for_each(cb)
          

  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

# i dont think I need to provide the cb

      # print(f"current",current.value)
      # print(f"currentleft",current.left.value)
      # print(f"currentright",current.right.value)