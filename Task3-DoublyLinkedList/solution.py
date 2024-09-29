class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DoubleLinkedList:
  def __init__(self):
    self.head = None

  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None, None)
      return
    itr = self.head
    while itr.next:
      itr = itr.next
    new_node = Node(data, None, itr)
    itr.next = new_node

  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count+=1
      itr = itr.next
    return count

  def insert_at(self, index, data):
    if index<0 or index >= self.get_length():
      raise Exception("Invalid index")
    if index == 0:
      self.insert_at_begining(data)
      return
    count = 0
    itr = self.head
    while itr:
      if count == index -1:
        node = Node(data, itr.next, itr)
        itr.next= node
        if node.next:
          node.next.prev = node
        break
      itr= itr.next
      count+=1

  def del_at_begining(self):
    self.head = self.head.next
    return

  def del_at_end(self):
    if self.head is None:
      return("This List is already empty")
    if self.head.next is None:
      self.head = None
      return
    itr = self.head
    while itr.next.next:
      itr = itr.next

    itr.next = None
    return

  def del_at(self, index):
    if index<0 or index >= self.get_length():
      raise Exception("Invalid index")
    if index == 0:
      self.del_at_begining()
      return
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        node_del = itr.next
        if node_del is None:
          return

        itr.next = node_del.next
        if node_del.next:
          node_del.next.prev = itr
        break
      itr = itr.next
      count+=1

  def traverse_forward(self):
    itr = self.head
    while itr:
      print(itr.data, end="")
      if itr.next:
          print(" <--> ", end="")
      else:
          print()
      itr = itr.next

  def traverse_backward(self):
    itr = self.head
    while itr.next:
      itr = itr.next
    while itr:
      print(itr.data, end="")
      if itr.prev:
          print(" <--> ", end="")
      else:
          print()
      itr = itr.prev

  def print(self):
    if self.head is None:
      print("Double Linked list is empty")
      return
    itr = self.head
    dlstr =''
    while itr:
      dlstr += str(itr.data) + '<-->'
      itr = itr.next
    print(dlstr)

if __name__ == '__main__':
  dl = DoubleLinkedList()
  dl.insert_at_begining(1)
  #dl.del_at_begining()
  dl.insert_at_begining(4)
  dl.insert_at(0,23)
  dl.insert_at_end(3)
  dl.insert_at_end(7)
  dl.insert_at_end(5)
  dl.del_at(1)
  dl.traverse_forward()
  dl.traverse_backward()
  dl.print()