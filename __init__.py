from typing import Callable, Optional

class DoubleLinkedListNode:
  """
  Doubly linked list built specifically for LRU cache
  """

  def __init__(self, key: int, val: int):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None
