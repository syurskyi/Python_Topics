#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Implement a queue using two stacks.

c_ Stack(
  ___  - (self
    li__  []
  
  ___ __len__(self
    r_ le_(li__)
  
  ___ push  item
    li__.ap..(item)
  
  ___ pop(self
    __ le_(li__) __ 0:
      r_ N..
    r_ li__.pop()

c_ QueueviaStack(
  ___  - (self
    inStack  Stack()
    outStack  Stack()
  
  ___ enqueue  item
    inStack.push(item)
  
  ___ dequeue(self
    w__ le_(inStack
      outStack.push(inStack.pop())
    result  outStack.pop()
    w__ le_(outStack
      inStack.push(outStack.pop())
    r_ result
  

customQueue  QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())