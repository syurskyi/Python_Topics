#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Implement a queue using two stacks.

class Stack(
  ___ __init__(self
    self.list = []
  
  ___ __len__(self
    r_ le_(self.list)
  
  ___ push(self, item
    self.list.append(item)
  
  ___ pop(self
    __ le_(self.list) == 0:
      r_ None
    r_ self.list.pop()

class QueueviaStack(
  ___ __init__(self
    self.inStack = Stack()
    self.outStack = Stack()
  
  ___ enqueue(self, item
    self.inStack.push(item)
  
  ___ dequeue(self
    while le_(self.inStack
      self.outStack.push(self.inStack.pop())
    result = self.outStack.pop()
    while le_(self.outStack
      self.inStack.push(self.outStack.pop())
    r_ result
  

customQueue = QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())