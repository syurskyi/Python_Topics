#!/usr/bin/python3
"""
There are two kinds of threads, oxygen and hydrogen. Your goal is to group these
threads to form water molecules. There is a barrier where each thread has to
wait until a complete molecule can be formed. Hydrogen and oxygen threads will
be given releaseHydrogen and releaseOxygen methods respectively, which will
allow them to pass the barrier. These threads should pass the barrier in groups
of three, and they must be able to immediately bond with each other to form a
water molecule. You must guarantee that all the threads from one molecule bond
before any other threads from the next molecule do.

In other words:
If an oxygen thread arrives at the barrier when no hydrogen threads are
present, it has to wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present,
it has to wait for an oxygen thread and another hydrogen thread.
We don’t have to worry about matching the threads up explicitly; that is, the
threads do not necessarily know which other threads they are paired up with. The
key is just that threads pass the barrier in complete sets; thus, if we examine
the sequence of threads that bond and divide them into groups of three, each
group should contain one oxygen and two hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these
constraints.

Example 1:

Input: "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.
Example 2:

Input: "OOHHHH"
Output: "HHOHHO"
Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH",
"HOHOHH" and "OHHOHH" are also valid answers.

Constraints:

Total length of input string will be 3n, where 1 ≤ n ≤ 20.
Total number of H will be 2n in the input string.
Total number of O will be n in the input string.
"""
____ t___ _______ C..
____ threading _______ Semaphore

____ c.. _______ d..

c_ H2O:
    ___ -
        hq d..()
        oq d..()

    ___ hydrogen  releaseHydrogen: C..[[], N..]) __ N..
        hq.a..(releaseHydrogen)
        try_output()

    ___ oxygen  releaseOxygen: C..[[], N..]) __ N..
        oq.a..(releaseOxygen)
        try_output()

    ___ try_output
        __ l..(hq) >_ 2 a.. l..(oq) >_ 1:
            hq.popleft()()
            hq.popleft()()
            oq.popleft()()


c_ H2O_TLE2:
    ___ -
        """
        Conditional Variable as counter? - Semaphore
        """
        gates [Semaphore(2), Semaphore(0)]  # inititally allow 2 H, 0 O

    ___ hydrogen  releaseHydrogen: C..[[], N..]) __ N..
        gates[0].a..
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        __ gates[0].acquire(blocking=F..  # self.gates[0]._value > 0
            # still have available count
            gates[0].release()
        ____
            gates[1].release()


    ___ oxygen  releaseOxygen: C..[[], N..]) __ N..
        gates[1].a..
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        gates[0].release()
        gates[0].release()


c_ H2O_TLE:
    ___ -
        """
        Conditional Variable as counter?
        Fixed at HHO pattern
        """
        h_cnt 0
        locks [Lock() ___ _ __ r..(3)]
        locks[1].a..


    ___ hydrogen  releaseHydrogen: C..[[], N..]) __ N..
        locks[0].a..
        h_cnt += 1
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        __ h_cnt < 2:
            locks[0].release()
        ____
            locks[1].release()


    ___ oxygen  releaseOxygen: C..[[], N..]) __ N..
        locks[1].a..
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        h_cnt 0
        locks[0].release()
