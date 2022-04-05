#!/usr/bin/python3
"""
uppose you are given the following code:

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // constructor
  public void zero(printNumber) { ... }  // only output 0's
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A will call zero() which should only output 0's.
Thread B will call even() which should only ouput even numbers.
Thread C will call odd() which should only output odd numbers.
Each of the threads is given a printNumber method to output an integer. Modify
the given program to output the series 010203040506... where the length of the
series must be 2n.


Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them
calls zero(), the other calls even(), and the last one calls odd(). "0102" is
the correct output.
Example 2:

Input: n = 5
Output: "0102030405"
"""
____ t___ _______ C..
____ threading _______ Lock


c_ ZeroEvenOdd:
    ___ - , n
        """
        only use 3 locks, and zero() knows and commonds which lock to release,
        determing whether even() or odd() will run.
        """
        n = n
        locks = [Lock() ___ _ __ r..(3)]
        locks[1].a..
        locks[2].a..

	# printNumber(x) outputs "x", where x is an integer.
    ___ zero  printNumber: C..[[i..], N..]) __ N..
        ___ i __ r..(n
            locks[0].a..
            printNumber(0)
            __ (i + 1) % 2 __ 1:
                locks[1].release()
            ____
                locks[2].release()

    ___ odd  printNumber: C..[[i..], N..]) __ N..
        ___ i __ r..((n + 1) // 2
            locks[1].a..
            printNumber(i * 2 + 1)
            locks[0].release()

    ___ even  printNumber: C..[[i..], N..]) __ N..
        ___ i __ r..(n // 2
            locks[2].a..
            printNumber(i * 2 + 2)
            locks[0].release()


c_ ZeroEvenOddError:
    ___ - , n
        """
        Like 1115, two layer of locks can do: zero and non-zero alternating,
        odd and even alternating. 4 locks required.

        Using only 3 locks?
        """
        n = n
        locks = [Lock(), Lock(), Lock(), Lock()]
        ___ i __ r..(1, l..(locks:
            locks[i].a..

	# printNumber(x) outputs "x", where x is an integer.
    ___ zero  printNumber: 'Callable[[int], None]') __ N..
        w__ locks[0]:
            printNumber(0)

    ___ even  printNumber: 'Callable[[int], None]') __ N..
        # cannot lock self.locks[1] from both "even" and "odd"
        p..


    ___ odd  printNumber: 'Callable[[int], None]') __ N..
        p..
