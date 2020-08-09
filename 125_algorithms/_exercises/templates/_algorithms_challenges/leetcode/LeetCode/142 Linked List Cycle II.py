"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node
    ___ detectCycle(self, head
        """
        if extra space available, hash table
        if not, use the model of Hare and Tortoise

        x = initial list size before cycle
        y = circle size

        When hare and tortoise meet, the hare totally runs: x+hy+m. The tortoise totally runs: x+ty+m
        Because x+hy+m = 2(x+ty+m)
        Thus, ky = 2ty+x+m we have (x+m) mod y = 0 We can conclude that if the tortoise runs more x steps, it will reach\
        the cycle's starting node, w___ x is the initial list size before cycle.
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
        flag = False
        w___ hare and hare.next and tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            __ hare__tortoise:
                flag = True
                break

        __ not flag:
            r_ None

        # run more x steps
        cur = head
        w___ cur:
            __ cur__tortoise:
                break
            cur = cur.next
            tortoise = tortoise.next

        r_ cur