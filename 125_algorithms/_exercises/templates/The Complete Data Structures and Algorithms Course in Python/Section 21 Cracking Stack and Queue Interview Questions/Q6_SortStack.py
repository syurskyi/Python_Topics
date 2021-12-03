#   Created by Elshad Karimov on 02/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Sort a stack with the smallest on top using only a single temporary stack.

___ sort_stack(stack
  previous = stack.pop()
  current = stack.pop()
  temp = Stack()
  w__ current:
    __ previous < current:
      temp.push(previous)
      previous = current
      current = stack.pop()
    ____
      temp.push(current)
      current = stack.pop()
    __ current __ N.. a__ previous: temp.push(previous)
       
  sorted = T..
  previous = temp.pop()
  current = temp.pop()
  w__ current:
    __ previous > current:
      stack.push(previous)
      previous = current
      current = temp.pop()
    ____
      stack.push(current)
      current = temp.pop()
      sorted = F..
    __ current __ N.. a__ previous: stack.push(previous)
  __ sorted: r_ stack
  ____ r_ sort_stack(stack)

c_ Stack(
  ___  - (self
    top = N..
  
  ___ __str__(self
    r_ st.(top)
  
  ___ push  item
    top = current(item, top)
  
  ___ pop(self
    __ no. top:
      r_ N..
    item = top
    top = top.next
    r_ item.data

c_ current(
  ___  -   data=N.., next=N..
    data, next = data, next
  
  ___ __str__(self
    r_ st.(self a__ data) + ',' + st.(self a__ next)

_____ unittest

c_ Test(unittest.TestCase
  ___ test_sort_stack(self
    assertEqual(st.(sort_stack(Stack())), "None")
    stack = Stack()
    stack.push(10)
    stack.push(30)
    stack.push(70)
    stack.push(40)
    stack.push(80)
    stack.push(20)
    stack.push(90)
    stack.push(50)
    stack.push(60)
    assertEqual(st.(stack), "60,50,90,20,80,40,70,30,10,None")
    assertEqual(st.(sort_stack(stack)), "10,20,30,40,50,60,70,80,90,None")

unittest.main()