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
will call foo() while thread B will call bar(). Modify the given program to
output "foobar" n times.



Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls
foo(), while the other calls bar(). "foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.
"""
____ threading _______ Lock
____ t___ _______ C..


c_ FooBar:
    ___ - , n
        n n
        locks [Lock(), Lock()]
        locks[1].a..


    ___ foo  printFoo: C..[[], N..]) __ N..
        ___ i __ r..(n
            locks[0].a..
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            locks[1].release()


    ___ bar  printBar: C..[[], N..]) __ N..
        ___ i __ r..(n
            locks[1].a..
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            locks[0].release()
