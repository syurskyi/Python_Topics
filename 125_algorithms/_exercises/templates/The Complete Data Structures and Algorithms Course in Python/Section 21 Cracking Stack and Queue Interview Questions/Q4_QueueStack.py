#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Implement a queue using two stacks.

c_ Stack(
  ___  - (self
    list = []
  
  ___ __len__(self
    r_ le_(list)
  
  ___ push  item
    list.ap..(item)
  
  ___ pop(self
    __ le_(list) __ 0:
      r_ N..
    r_ list.pop()

c_ QueueviaStack(
  ___  - (self
    inStack = Stack()
    outStack = Stack()
  
  ___ enqueue  item
    inStack.push(item)
  
  ___ dequeue(self
    while le_(inStack
      outStack.push(inStack.pop())
    result = outStack.pop()
    while le_(outStack
      inStack.push(outStack.pop())
    r_ result
  

customQueue = QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())