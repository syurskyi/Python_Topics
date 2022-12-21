c_ TwoSum o..

    ___ - ____:
        """
        initialize your data structure here
        """
        internal =    # list
        dic  # dict

    ___ add  number
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        internal.append(number)
        __ number __ dic:
            # more than once
            dic[number] = T..
            r_
        # once
        dic[number] = F..

    ___ find  value
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        ___ v __ internal:
            __ value - v __ dic:
                __ v << 1 __ value and n.. dic[v]:
                    c_
                r_ T..
        r_ F..


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
