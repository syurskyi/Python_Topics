"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x):
        val = x
        next = N..


c_ Solution:
    # @param head, a ListNode
    # @return a list node
    ___ detectCycle  head):
        """
        if extra space available, hash table
        if not, use the model of Hare and Tortoise

        x = initial list size before cycle
        y = circle size

        When hare and tortoise meet, the hare totally runs: x+hy+m. The tortoise totally runs: x+ty+m
        Because x+hy+m = 2(x+ty+m)
        Thus, ky = 2ty+x+m we have (x+m) mod y = 0 We can conclude that if the tortoise runs more x steps, it will reach\
        the cycle's starting node, while x is the initial list size before cycle.
                                ____     ____
                              /'    |   |    \
                            /    /  |   | \   \
                          /    / |  |   |  \   \
                         (   /   |  ''''   |\   \
                         | /   / /^\    /^\  \  _|
                          ~   | |   |  |   | | ~
                              | |__O|__|O__| |
                            /~~      \/     ~~\
                           /   (      |      )  \
                     _--_  /,   \____/^\___/'   \  _--_
                   /~    ~\ / -____-|_|_|-____-\ /~    ~\
                 /________|___/~~~~\___/~~~~\ __|________\
            --~~~          ^ |     |   |     |  -     :  ~~~~~:~-_     ___-----~~~~|
               /             `^-^-^'   `^-^-^'                  :  ~\ /'   ____/----|
                   --                                            ;   |/~~~------~~~~~|
             ;                                    :              :    |------/--------|
            :                     ,                           ;    .  |---\\----------|
             :     -                          .                  : : |__________-__|
              :              ,                 ,                :   /'~----_______|
            __  \\\        ^                          ,, ;; ;; ;._-~
              ~~~-----____________________________________----~~~

        :param head: ListNode
        :return: ListNode
        """

        # find cycle
        hare = head
        tortoise = head
        flag = F..
        w.... hare a.. hare.next a.. tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            __ hare__tortoise:
                flag = T..
                _____

        __ n.. flag:
            r.. N..

        # run more x steps
        cur = head
        w.... cur:
            __ cur__tortoise:
                _____
            cur = cur.next
            tortoise = tortoise.next

        r.. cur