c_ Solution o..
    ___ isStrobogrammatic  num):
        """
        :type num: str
        :rtype: bool
        """
        # hash table
        dic = {'0':'0', '6':'9', '9': '6', '1' :'1', '8': '8'}
        temp_s = ''
        ___ c __ num[::-1]:
            __ c not __ dic:
                r_ False
            temp_s += dic[c]
        __ int(temp_s) __ int(num):
            r_ True
        r_ False

    # def isStrobogrammatic(self, num):
    #     # https://discuss.leetcode.com/topic/20840/1-liners-python
    #     return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)/2+1))
        