"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x
        val = x
        next = N..

c_ Solution:
    ___ hasCycle  head
        """
        if extra space available, use hash table
        if not, use the model of Hare and Tortoise
        Algorithm:
        Hare & Tortoise
        Physics, relative velocity.
                                       ___-------___
                                   _-~~             ~~-_
                                _-~                    /~-_
             /^\__/^\         /~  \                   /    \
           /|  O|| O|        /      \_______________/        \
          | |___||__|      /       /                \          \
          |          \    /      /                    \          \
          |   (_______) /______/                        \_________ \
          |         / /         \                      /            \
           \         \^\\         \                  /               \     /
             \         ||           \______________/      _-_       //\__//
               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \_\      \.
                         (_(___/                         \_____)_)

        :param head: ListNode
        :return: boolean
        """
        hare = head
        tortoise = head
        w.... hare a.. hare.next a.. tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            __ hare__tortoise:
                r.. T..

        r.. F..
