from Node import Node

class Stack:
  def __init__(self, limit = 10000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item_to_add = Node(value)
      item_to_add.set_next_node(self.top_item)
      self.top_item = item_to_add
      self.size += 1
      print("Adding {} to the stack.".format(value))
    else:
      print("The stack is currently full.")

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Removing " + item_to_remove.get_value() + ".")
      return item_to_remove.get_value()
    else:
      print("The stack is currently empty.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    else:
      print("The stack is currently empt.")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0