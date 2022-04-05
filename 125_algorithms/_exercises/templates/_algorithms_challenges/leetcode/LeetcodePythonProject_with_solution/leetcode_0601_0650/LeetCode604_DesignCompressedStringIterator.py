'''
Created on Sep 6, 2017

@author: MT
'''
c_ StringIterator(o..

    ___ - , compressedString
        """
        :type compressedString: str
        """
        cmpStr = compressedString
        count = 0
        ind = 0
        __ cmpStr:
            c = cmpStr[ind]
            ind += 1
            w.... ind < l..(cmpStr) a.. cmpStr[ind].i..
                ind += 1
            count = i..(cmpStr[1:ind])

    ___ next
        """
        :rtype: str
        """
        res = c
        count -_ 1
        __ count __ 0:
            __ ind __ l..(cmpStr
                c = ' '
                r.. res
            c = cmpStr[ind]
            ind += 1
            ind = ind
            w.... ind < l..(cmpStr) a.. cmpStr[ind].i..
                ind += 1
            count = i..(cmpStr[ind:ind])
            ind = ind
        r.. res

    ___ hasNext
        """
        :rtype: bool
        """
        r.. c != ' '

__ _____ __ _____
    it = StringIterator('L1e2t1C1o1d1e1')
    w.... it.hasNext
        print(it.next
