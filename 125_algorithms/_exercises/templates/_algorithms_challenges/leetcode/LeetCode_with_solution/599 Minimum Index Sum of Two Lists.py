#!/usr/bin/python3
"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both
have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index
sum. If there is a choice tie between answers, output all of them with no order
requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
____ typing _______ List


c_ Solution:
    ___ findRestaurant  list1: List[s..], list2: List[s..]) __ List[s..]:
        index    # dict
        ___ i, v __ e..(list2
            index[v] = i

        ret    # list
        mini = f__('inf')
        ___ i, v __ e..(list1
            __ v __ index:
                cur = i + index[v]  # current index sum
                __ cur < mini:
                    mini = cur
                    ret = [v]
                ____ cur __ mini:
                    ret.a..(v)

        r.. ret
