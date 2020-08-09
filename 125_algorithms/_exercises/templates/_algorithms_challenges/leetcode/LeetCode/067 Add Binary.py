__author__ = 'Danyang'
class Solution:
    ___ addBinary_builtin(self, a, b
        """
        Built-in function
        :param a: string
        :param b: string
        :return: string
        """
        a = int(a, 2)
        b = int(b, 2)
        r_ bin(a+b)[2:]

    ___ addBinary(self, a, b
        """
        Built-in function
        :param a: string
        :param b: string
        :return: string
        """
        __ le.(a)>le.(b
            a, b = b, a

        a, b = list(a), list(b)

        # from LSB to MSB
        a.reverse()
        b.reverse()
        # b as the base number
        ___ i in xrange(le.(a)):
            __ a[i]__"0":  # 0
                continue
            ____ b[i]__"0":  # 0+1
                b[i] = "1"
                continue
            ____  # 1+1
                b[i] = "0"

                # carry forward
                __ i__le.(b)-1:
                    b.append("1")
                ____
                    ___ j in range(i+1, le.(b)):
                        __ b[j]__"0":
                            b[j] = "1"
                            break

                        ____
                            b[j] = "0"  # carry forward
                            __ j__le.(b)-1:
                                b.append("1")
                                break

        b.reverse()
        r_ "".join(b)  # reversed back

__ __name____"__main__":
    print Solution().addBinary("11", "1")
