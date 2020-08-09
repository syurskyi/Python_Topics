'''
Created on Sep 6, 2017

@author: MT
'''
class StringIterator(object

    ___ __init__(self, compressedString
        """
        :type compressedString: str
        """
        self.cmpStr = compressedString
        self.count = 0
        self.ind = 0
        __ self.cmpStr:
            self.c = self.cmpStr[self.ind]
            self.ind += 1
            w___ self.ind < le.(self.cmpStr) and self.cmpStr[self.ind].isdigit(
                self.ind += 1
            self.count = int(self.cmpStr[1:self.ind])

    ___ next(self
        """
        :rtype: str
        """
        res = self.c
        self.count -= 1
        __ self.count __ 0:
            __ self.ind __ le.(self.cmpStr
                self.c = ' '
                r_ res
            self.c = self.cmpStr[self.ind]
            self.ind += 1
            ind = self.ind
            w___ ind < le.(self.cmpStr) and self.cmpStr[ind].isdigit(
                ind += 1
            self.count = int(self.cmpStr[self.ind:ind])
            self.ind = ind
        r_ res

    ___ hasNext(self
        """
        :rtype: bool
        """
        r_ self.c != ' '

__ __name__ __ '__main__':
    it = StringIterator('L1e2t1C1o1d1e1')
    w___ it.hasNext(
        print(it.next())
