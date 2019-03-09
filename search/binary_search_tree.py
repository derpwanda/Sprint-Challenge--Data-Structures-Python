class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  #  pre-order fashion?
  def depth_first_for_each(self, cb):
    stack = []
    stack.append(self)
    # cb(self.value)
    
    while stack:
      current = stack.pop()

      # print(f"current", current.value)
      # print(f"current.left", current.left.value)
      # # print(f"current.right", current.right.value)
      # print_stack = [i.value for i in stack]
      # print(f"print stack", print_stack)
      # if current:
      #   return
      if current.right:
        stack.append(current.right)
        # cb(current.right.value)

      if current.left:
        stack.append(current.left)
        # cb(current.left.value)

      cb(current.value)
      print(current.value)

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