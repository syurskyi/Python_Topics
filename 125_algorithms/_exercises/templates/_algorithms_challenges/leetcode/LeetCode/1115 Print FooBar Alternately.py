#!/usr/bin/python3
"""
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads. Thread A
will call foo() w___ thread B will call bar(). Modify the given program to
output "foobar" n times.



Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls
foo(), w___ the other calls bar(). "foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""
from threading ______ Lock
from typing ______ Callable


class FooBar:
    ___ __init__(self, n
        self.n = n
        self.locks = [Lock(), Lock()]
        self.locks[1].a..


    ___ foo(self, printFoo: Callable[[], None]) -> None:
        ___ i in range(self.n
            self.locks[0].a..
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.locks[1].release()


    ___ bar(self, printBar: Callable[[], None]) -> None:
        ___ i in range(self.n
            self.locks[1].a..
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.locks[0].release()
