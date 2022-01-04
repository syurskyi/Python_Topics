__author__ = 'Danyang'
c_ Solution:
    ___ addBinary_builtin(self, a, b):
        """
        Built-in function
        :param a: string
        :param b: string
        :return: string
        """
        a = i..(a, 2)
        b = i..(b, 2)
        r.. bin(a+b)[2:]

    ___ addBinary(self, a, b):
        """
        Built-in function
        :param a: string
        :param b: string
        :return: string
        """
        __ l..(a)>l..(b):
            a, b = b, a

        a, b = l..(a), l..(b)

        # from LSB to MSB
        a.reverse()
        b.reverse()
        # b as the base number
        ___ i __ xrange(l..(a)):
            __ a[i]__"0":  # 0
                _____
            ____ b[i]__"0":  # 0+1
                b[i] = "1"
                _____
            ____:  # 1+1
                b[i] = "0"

                # carry forward
                __ i__len(b)-1:
                    b.a..("1")
                ____:
                    ___ j __ r..(i+1, l..(b)):
                        __ b[j]__"0":
                            b[j] = "1"
                            break

                        ____:
                            b[j] = "0"  # carry forward
                            __ j__len(b)-1:
                                b.a..("1")
                                break

        b.reverse()
        r.. "".j..(b)  # reversed back

__ __name____"__main__":
    print Solution().addBinary("11", "1")
